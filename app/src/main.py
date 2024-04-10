import os, sys
from unidecode import unidecode

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from helpers.LogConfig import LogConfig
from helpers.Words import Words

if __name__ == "__main__":
    LogConfig()
    while (
        not (
            text := str(
                input("Deixe seu comentário ou digite 'sair' para sair: ").strip()
            )
        )
        in "sair"
    ):
        word = Words(text=unidecode(text))
        word.classify_word()
