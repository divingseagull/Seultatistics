import json
from enum import Enum
import os


class TokenStorageType(Enum):
    SYS_ENV = "SYS_ENV"
    FILE = "FILE"


class Config:
    def __init__(self,
                 config_path: int | str | bytes | os.PathLike[str] | os.PathLike[bytes] = "config.json",
                 encoding: str = 'utf-8'):
        with open(config_path, 'r', encoding=encoding) as config_reader:
            self.__data = json.load(config_reader)

    def get_bot_config(self) -> dict:
        return self.__data["bot"]

    def get_token(self) -> str:
        bot_token_config = self.get_bot_config()['token']

        if bot_token_config['storage_type'] == TokenStorageType.SYS_ENV.value:
            path = bot_token_config['path']
            token = os.environ.get(path)
            return token
        elif bot_token_config['storage_type'] == TokenStorageType.FILE.value:
            with open(bot_token_config['path'], 'r') as token_reader:
                token = token_reader.read().strip()
                return token

    def get_owner_ids(self) -> list[int]:
        owner_ids = self.get_bot_config()['owner_ids']
        return owner_ids

    def get_available_server_ids(self) -> list[int]:
        available_ids = self.get_bot_config()['available_server_ids']
        return available_ids

    def get_log_config(self):
        log_config = self.get_bot_config()['log']
        return log_config

    def get_extension_config(self):
        ext_config = self.__data["extensions"]
        return ext_config
