import os, sys, requests  # , nltk
from bs4 import BeautifulSoup
from typing import List
from loguru import logger
from nltk.util import ngrams
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from unidecode import unidecode


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from .ChangeFiles import ChangeFiles
from resource.configs.settings import LINK_SITE_TO_SWEARINGS, LINK_SITE_TO_COMPLIMENTS
from resource.constraints import H2_STRING_ELEMENT, COMPLAINTS_KEYWORDS

# nltk.download("vader_lexicon")
# nltk.download('punkt')
# nltk.download('stopwords')


class Words:
    def __init__(self: object, text: str = " ") -> None:
        self.text = text
        self.swearings = self.capture_swearings()
        self.complaints = self.capture_complaints()
        self.compliments = self.capture_compliments()

    def capture_swearings(self: object) -> List[str] | bool:
        """Função responsável por capturar palávras imprópias"""
        url = LINK_SITE_TO_SWEARINGS
        response = requests.get(url)

        swearings = []
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            h2_element = soup.find("h2", string=H2_STRING_ELEMENT)
            if h2_element:
                ul_element = h2_element.find_next("ul")
                if ul_element:
                    for li_element in ul_element.find_all("li"):
                        swearings.append(li_element.text.lower())
        else:
            logger.error("Erro ao acessar a página:", response.status_code)
            return False

        unidecode_swearings = []
        for swearing in swearings:
            unidecode_swearings.append(unidecode(swearing.lower()))

        logger.success("Palavras Imprópias capturadas com sucesso")
        return swearings

    def capture_complaints(self: object) -> bool:
        """Função responsável por capturar palávras que expressão uma reclamação"""

        stop_words = set(stopwords.words("portuguese"))

        def has_complaint_bigram(bigram):
            for keyword in COMPLAINTS_KEYWORDS:
                if keyword in bigram:
                    return True
            return False

        tokens = word_tokenize(self.text.lower())
        tokens = [token for token in tokens if token not in stop_words]
        bigrams_list = list(ngrams(tokens, 1))

        for bigram in bigrams_list:
            if has_complaint_bigram(bigram):
                return True

        sia = SentimentIntensityAnalyzer()
        sentiment_score = sia.polarity_scores(self.text)
        if sentiment_score["neg"] > sentiment_score["pos"]:
            return True

        return False

    def capture_compliments(self: object) -> List[str] | bool:
        """Função responsável por capturar palávras que expressão um elogio"""
        url = LINK_SITE_TO_COMPLIMENTS
        response = requests.get(url)

        compliments = []
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            tables = soup.find_all("table")
            for table in tables:
                table_text = table.get_text(separator="\n", strip=True)
                table_text = table_text.lower().replace(";", "").replace(".", "")
                tables_content = table_text.split("\n")
                compliments.extend(tables_content)
        else:
            logger.error("Erro ao acessar a página:", response.status_code)
            return False

        unidecode_compliments = []
        for compliment in compliments:
            unidecode_compliments.append(unidecode(compliment.lower()))

        logger.success("Palavras que expressão elogios capturadas com sucesso")
        return unidecode_compliments

    def classify_word(self) -> str:
        if not len(self.text) > 1:
            logger.error("Palavra inválida! digite um palavra ou frase.")
            return "Palavra inválida! digite um palavra ou frase."
        elif any(word in self.text for word in self.swearings):
            file = ChangeFiles("palavras_impropias.txt")
            file.save_to_file(self.text)
            logger.info("Xingamento registrado :(")
            return "Xingamento registrado :("
        elif self.complaints:
            file = ChangeFiles("reclamacoes.txt")
            file.save_to_file(self.text)
            logger.info("Reclamação registrada...")
            return "Reclamação registrada..."
        elif any(word in self.text for word in self.compliments):
            file = ChangeFiles("elogios.txt")
            file.save_to_file(self.text)
            logger.info("Elogio registrado...")
            return "Elogio registrado..."
        else:
            file = ChangeFiles("palavras_desconhecidas.txt")
            file.save_to_file(self.text)
            logger.info(
                "A palavra não foi identificada. Iremos armazena-la para uso posterior"
            )
            return (
                "A palavra não foi identificada. Iremos armazena-la para uso posterior"
            )
