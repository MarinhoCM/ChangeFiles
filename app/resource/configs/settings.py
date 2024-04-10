import os
from loguru import logger
from dotenv import load_dotenv

load_dotenv()


try:
    LINK_SITE_TO_SWEARINGS = os.environ["LINK_SITE_TO_SWEARINGS"]
    LINK_SITE_TO_COMPLIMENTS = os.environ["LINK_SITE_TO_COMPLIMENTS"]
except KeyError as e:
    message = (
        f"Ocorreu um erro ao tentar carregar a váriavel de ambiente: {e}\n"
        + "Verifique se ela existe no arquivo '.env' presente em "
        + "'app//resource//configs'"
    )
    logger.error(message)
    raise KeyError(message)
else:
    logger.success("VARIÁVEIS DE AMBIENTE CARREGADAS COM SUCESSO")
