from .abstract_model import AbstractModel
from database.db import db


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data):
        super().__init__(data)

    def to_dict(self):
        # get é um método de dicts. Ele possibilita a obtenção de um valor
        # associado a uma chave específíca.
        # https://www.w3schools.com/python/ref_dictionary_get.asp
        return {
            "name": self.data.get("name"),
            "acronym": self.data.get("acronym"),
        }
