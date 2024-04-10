import nltk
from nltk.tokenize import word_tokenize

class SortWord:
    def __init__(self):
        self.text = str(input("Digite algo: "))

    def analyze_text(self):
        """
        Função responsável por interpretar um texto e identificar
        qual sua intenção.
        """
    