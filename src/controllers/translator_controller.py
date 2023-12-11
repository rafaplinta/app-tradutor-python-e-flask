from flask import Blueprint, render_template
from models.language_model import LanguageModel

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
