import os, sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from helpers.ChangeFiles import ChangeFiles
from helpers.LogConfig import LogConfig

if __name__ == "__main__":
    LogConfig()
    changer = ChangeFiles(".gitignore")
    changer.delete_file()
