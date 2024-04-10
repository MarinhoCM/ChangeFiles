import os, shutil, datetime
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

    def insert_text_in_file(self, text_to_change) -> bool:
        if self.verify_path_existence(self.file_name):
            with open(self.file_name, "a", encoding="utf-8") as file_content:
                file_content.write("\n" + text_to_change)
        else:
            with open(self.file_name, "a", encoding="utf-8") as file_content:
                file_content.write(text_to_change)

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

    def check_text_in_file(self, file_path: str, text: str) -> bool:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    if text in line.strip() and text in line.split(":")[-1].strip():
                        return True
        return False

    def save_to_file(self, text: str) -> None:
        folder = "classified_texts"
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        if not os.path.exists(folder):
            os.makedirs(folder)
        file_path = os.path.join(folder, self.file_name)
        if not self.check_text_in_file(file_path, text.strip()):
            with open(file_path, "a", encoding="utf-8") as file:
                file.write(f"{timestamp}:{text.strip()}\n")
        else:
            logger.info("O texto já foi armazenado anteriormente")

    @staticmethod
    def verify_path_existence(file_path: str) -> bool:
        if os.path.exists(str(file_path)):
            return True
        else:
            file_name = str(file_path).split("\\")[-1]
            logger.error(
                f"Não foi possivel encontrar o arquivo: {file_name}. O arquivo será criado."
            )
            return False

    def __str__(self) -> str:
        return """
        ChangeFiles():
            Função responsável por realizar interações e alterações em diretórios.
        """
