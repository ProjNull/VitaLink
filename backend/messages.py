from flask import Blueprint, jsonify, request
from middlecrud import get_messages, send_message

messages = Blueprint("Messages_BP", __name__, url_prefix="/messages")


@messages.route("/get")
def getMessages():
    idMessage = request.json.get("patientId")
    var = get_messages(idMessage)

    return jsonify({"messages": var if var else []})


@messages.route("/post")
def postMessages():
    idPatient = request.json.get("idPatient")
    idEmployee = request.json.get("idEmployee")
    isSenderEmployee = request.json.get("isSenderEmployee")
    content = request.json.get("content")
    repliesTo = request.json.get("repliesTo")

    var = send_message(idPatient, idEmployee, isSenderEmployee, content, repliesTo)

    return jsonify({"success": var})
