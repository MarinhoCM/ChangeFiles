import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from helpers.ChangeFiles import ChangeFiles

if __name__ == "__main__":
    changer = ChangeFiles(".gitignore")
    changer.delete_file()
