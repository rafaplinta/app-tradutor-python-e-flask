from flask import Blueprint, render_template, request
from models.language_model import LanguageModel
from models.history_model import HistoryModel
from deep_translator import GoogleTranslator

translator_controller = Blueprint("translator_controller", __name__)


@translator_controller.route("/", methods=["GET"])
def get_languages():
    # obtém a lista de idiomas usando o método list_dicts
    languages = LanguageModel.list_dicts()

    # variáveis para o template
    text_to_translate = "O que deseja traduzir?"
    translate_from = "pt"
    translate_to = "en"
    translated = "What do you want to translate?"

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


@translator_controller.route("/", methods=["POST"])
def translate_text():
    languages = LanguageModel.list_dicts()
    # request acessa os dados enviados em uma solicitação HTTP
    # a função get é utilizada para buscar as infos do formulário
    # dentro do () eu passo o name do form.
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    # instancia a history para salvar as traduções no histórico
    HistoryModel(
        {
            "text_to_translate": text_to_translate,
            "translate_from": translate_from,
            "translate_to": translate_to
        }
    ).save()

    # a biblioteca GoogleTranslator traduz o texto usando os idiomas de origem
    # e destino
    translated = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


@translator_controller.route("/reverse", methods=["POST"])
def reverse_translation():
    languages = LanguageModel.list_dicts()
    text_to_translate = request.form.get("text-to-translate")
    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    reversed_translated = GoogleTranslator(
        source=translate_from,
        target=translate_to,
    ).translate(text_to_translate)

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=reversed_translated,
        translate_from=translate_to,
        translate_to=translate_from,
        translated=text_to_translate,
    )
