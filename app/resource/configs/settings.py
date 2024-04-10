import os
from loguru import logger
from dotenv import load_dotenv

load_dotenv()


try:
    LINK_SITE_TO_SWEARINGS = os.environ["LINK_SITE_TO_SWEARINGS"]
    LINK_SITE_TO_COMPLIMENTS = os.environ["LINK_SITE_TO_COMPLIMENTS"]
    logger.success("VARIÁVEIS DE AMBIENTE CARREGADAS COM SUCESSO")
except KeyError as e:
    raise KeyError(f"Ocorreu um erro ao tentar carregar a váriavel de ambiente: {e}")
