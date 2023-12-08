from flask import Blueprint, jsonify, request
from Database.employee_models import Employees
from Database.database import Session

employee = Blueprint("Nurses_BP", __name__, url_prefix="/nurses")

session_instance = Session()

@employee.route("/new", methods=["POST"])
def addEmployee():
    if request.method == "POST":
        firstName = request.json.get("firstName")
        lastName = request.json.get("lastName")
        nick = request.json.get("nick")
        password = request.json.get("password")
        dateOfBirth = request.json.get("dateOfBirth")
        isAdmin = request.json.get("isAdmin")
        q = session_instance.query(Employees).filter_by(nick).first()
        
        if q == nick:
            return jsonify({"message": "Someone already has this nickname!"})
        
        if not firstName or not lastName or not nick or not password or not dateOfBirth or not isAdmin: # TODO: Make list instead
            return jsonify({"message": "No, or incorrect params given!"})
        
        commitObject = Employees(
            firstName = firstName,
            lastName = lastName,
            nick = nick,
            password = password,
            dateOfBirth = dateOfBirth,
            isAdmin = isAdmin
        )
        session_instance.add(commitObject)
    return jsonify({"message": "Only POST enabled"})