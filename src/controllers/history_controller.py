from flask import Blueprint, jsonify
from models.history_model import HistoryModel

history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/", methods=["GET"])
def get_history():
    # obtém o histórico de traduções
    histories = HistoryModel.list_as_json()
    return jsonify(histories), 200
