import json
import os
import copy


class Config:
    def __init__(self,
                 config_path: str | os.PathLike[str],
                 encoding: str = 'utf-8'):
        self.config_path = config_path
        self.encoding = encoding

    def get_data(self) -> dict:
        with open(self.config_path, 'r', encoding=self.encoding) as config_io:
            data = json.load(config_io)
            data_copy = copy.deepcopy(data)
        return data_copy
