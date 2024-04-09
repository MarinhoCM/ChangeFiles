import os

from loguru import logger
from datetime import datetime

directory = os.path.dirname(os.path.abspath(__file__)).split("\\")
directory.pop()
SCRIPT_DIR = "\\".join(directory)


class LogConfig:
    def __init__(self, log_path=f"{SCRIPT_DIR}/resource/logs/", log_level="INFO"):
        self.log_path = log_path
        self.log_level = log_level
        self.configure_logger()

    def configure_logger(self):
        logger.remove()
        logger.add(
            self.log_path + f"{datetime.now().strftime('%Y-%m-%d')}.log",
            level=self.log_level,
            rotation="500 MB",
        )
        logger.add(
            self.log_path + f"{datetime.now().strftime('%Y-%m-%d')}_errors.log",
            level="ERROR",
            rotation="500 MB",
        )
