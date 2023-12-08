from flask import Blueprint, jsonify, request
from middlecrud import delete_patient, register_patient, login_patient, get_patient, set_patient_nickname

patients = Blueprint("Patients_BP", __name__, url_prefix="/patients")


def is_missing_params(parameters) -> bool:
    return not (None in parameters)


@patients.route("/create", methods=["POST"])
def addPatient():
    firstName = request.json.get("firstName")
    lastName = request.json.get("lastName")
    password = request.json.get("password")
    dateOfBirth = request.json.get("dateOfBirth")

    if is_missing_params([firstName, lastName, password, dateOfBirth]):
        return jsonify({"message": "Missing param", "status": 400})
    r = register_patient(firstName, lastName, dateOfBirth, password)
    if not r:
        return {"message": "Could not register", "status": 500}
    return {
        "message": "Registered!",
        "status": 200,
        "token": "payload.algorithm.signature",
    }


@patients.route("/get", methods=["GET"])
def getPatientByID():
    idPatient = request.json.get("idPatient")
    if not idPatient:
        return {"message": "Missing params", "status": 400}
    p = get_patient(idPatient)
    if not p:
        return {"message": "Patient could not be retrieved", "status": 500}
    return {"message": "Patient retrieved", "status": 200, "patient": p}

# TODO: login
@patients.route("/login", methods=["POST"])
def loginPatient():
    firstName = request.json.get("firstName")
    lastName = request.json.get("lastName")
    dateOfBirth = request.json.get("dateOfBirth")
    password = request.json.get("password")
    
    val = login_patient(firstName=firstName, lastName=lastName, dob=dateOfBirth, password=password)
    
    return jsonify(val)
# TODO: delete
@patients.route("/delete", methods=["DELETE"])
def deletePatient():
    idPatient = request.json.get("/idPatient")
    
    var = delete_patient(idPatient)
    
    return jsonify(var)
# TODO: set nickname
@patients.route("/put", methods=["PUT"])
def renamePatient():
    idPatient = request.json.get("idPatient")
    newNick = request.json.get("newNick")
    
    var = set_patient_nickname(idPatient, newNick)
    return jsonify(var)