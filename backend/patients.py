from flask import Blueprint, jsonify, request
from Database.database import Session

patients = Blueprint("Patients_BP", __name__, url_prefix="/patients")

session_instance = Session()

@patients.route("/create", methods=["POST"])
def addEmployee():
    if request.method == "GET": return jsonify({"message": "Only POST enabled"})

    params = request.json.get("params")
    
    if not params: 
        return jsonify({"message": "Missing param"})
    
    return jsonify()
