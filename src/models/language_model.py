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

    @classmethod
    def list_dicts(cls):
        # obtém um objeto iterável que veio da consulta find()
        # na coleção associada à classe.
        languages = cls._collection.find()

        # lista vazia para guardar os dicionários
        languages_list = []

        # para cada linguagem na nossa lista iterável de linguages
        for language in languages:
            # cria uma nova instância da classe LanguageModel
            # para representar o idioma.
            new_language = cls(language)

            # converte a instância do idioma para um dicionário
            # (com a função to_dict) e adiciona à lista.
            languages_list.append(new_language.to_dict())

        return languages_list
