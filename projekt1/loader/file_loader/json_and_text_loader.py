from abc import ABC, abstractmethod
import json
import re


class DataLoader(ABC):
    @abstractmethod
    def load(self, path: str) -> list[str]:
        pass


class JsonDataLoader(DataLoader):
    SUPPORTED_EXTENSION = '.json'

    def load(self, path: str) -> list[str]:
        if not path.endswith(JsonDataLoader.SUPPORTED_EXTENSION):
            raise AttributeError('File has incorrect extension')

        try:
            with open(path, 'r') as f:
                return json.load(f)
        except Exception as e:
            raise FileNotFoundError(f'File not found: {e}')

