import os, sys, requests
from bs4 import BeautifulSoup
from typing import List
from loguru import logger

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from resource.configs.settings import LINK_SITE_TO_SWEARINGS, LINK_SITE_TO_COMPLIMENTS
from resource.constraints import H2_STRING_ELEMENT


class Words:
    def __init__(self) -> None:
        self.swearings = self.capture_swearings()
        self.complaints = []
        self.compliments = self.capture_compliments()

    def capture_swearings(self: object) -> List[str] | bool:
        """Função responsável por capturar palávras imprópias"""
        url = LINK_SITE_TO_SWEARINGS
        response = requests.get(url)

        swearing = []
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            h2_element = soup.find("h2", string=H2_STRING_ELEMENT)
            if h2_element:
                ul_element = h2_element.find_next("ul")
                if ul_element:
                    for li_element in ul_element.find_all("li"):
                        swearing.append(li_element.text)
        else:
            logger.error("Erro ao acessar a página:", response.status_code)
            return False

        logger.success("Palavras Imprópias capturadas com sucesso")
        return swearing

    def capture_complaints(self: object) -> List[str]:
        """Função responsável por capturar palávras que expressão uma reclamação"""
        pass

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
                table_text = table_text.replace(";", "").replace(".", "")
                tables_content = table_text.split("\n")
                compliments.extend(tables_content)
        else:
            logger.error("Erro ao acessar a página:", response.status_code)
            return False

        logger.success("Palavras que expressão elogios capturadas com sucesso")
        return compliments


if __name__ == "__main__":
    words = Words()
    print(words.swearings)
    print("\n\n\n")
    print(words.compliments)
