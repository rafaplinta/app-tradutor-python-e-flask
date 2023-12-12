import json
from src.models.history_model import HistoryModel


# recebe prepare_base como argumento para os testes
def test_request_history(prepare_base):
    history_model = HistoryModel.list_as_json()
    # converte o JSON retornado para um objeto Python usando json.loads
    json_data = json.loads(history_model)

    assert len(json_data) == 2

    first_item = json_data[0]

    # verifica se as chaves existem
    assert "text_to_translate" in first_item
    assert "translate_from" in first_item
    assert "translate_to" in first_item

    # verifica se os valores correspondem ao esperado
    assert first_item["text_to_translate"] == "Hello, I like videogame"
    assert first_item["translate_from"] == "en"
    assert first_item["translate_to"] == "pt"
