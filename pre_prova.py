import os, shutil
from loguru import logger


class ChangeFiles:
    def __init__(self, file_name) -> None:
        self.file_name = file_name

    def get_text_in_file(self) -> str:
        if self.verify_path_existence(self.file_name):
            with open(str(self.file_name), "r", encoding="utf-8") as file_content:
                text = file_content.read()
                if text:
                    logger.success(f"Texto extraido do arquivo: \n{text}")
                    return text

    def insert_text_in_file(self) -> bool:
        if self.verify_path_existence(self.file_name):
            with open(self.file_name, "a", encoding="utf-8") as file_content:
                text_to_change = str(input("Digite o texto que deseja inserir: "))
                file_content.write("\n" + text_to_change)

    def delete_file(self) -> bool:
        if self.verify_path_existence(self.file_name):
            os.remove(self.file_name)
            if not os.path.exists(self.file_name):
                logger.info("Sucesso ao remover arquivo.")
                return True
            else:
                logger.error("O arquivo não foi removido")
                return False

    def delete_folder(self) -> bool:
        folder_path = str(input("Digite o nome da pasta que deseja deletar: "))
        if self.verify_path_existence(folder_path):
            shutil.rmtree(folder_path)
            if os.path.exists(self.file_name):
                logger.success("Pasta removida com sucesso!")
                return True
            else:
                logger.error(
                    "Não foi possivel remover a pasta. Tente utilizar 'delete_all_folders()'"
                )
                return False

    @staticmethod
    def verify_path_existence(file_path) -> bool:
        if os.path.exists(str(file_path)):
            return True
        else:
            file_name = str(file_path).split("\\")[-1]
            logger.error(f"Não foi possivel encontrar o arquivo: {file_name}")
            return False


files = ChangeFiles(r".gitignore")
# files.get_text_in_file()
files.delete_folder()
# files.insert_text_in_file()
