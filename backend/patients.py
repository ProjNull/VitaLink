from flask import Blueprint, jsonify, request
from Database.patient_models import Patients
from Database.database import Session

patients = Blueprint("Patients_BP", __name__, url_prefix="/patients")

session_instance = Session()

def is_missing_params(parameters) -> bool:
    for parameter in parameters:
        if parameters:
            return True
    return False

@patients.route("/create", methods=["POST"])
def addEmployee():
    if request.method == "GET": return jsonify({"message": "Only POST enabled"})

    params = request.json.get("params")

    firstName = request.json.get("firstName")
    lastName = request.json.get("lastName")
    password = request.json.get("password")
    dateOfBirth = request.json.get("dateOfBirth")
    
    if is_missing_params([firstName, lastName, password, dateOfBirth]):
        return jsonify({"message": "Missing param"})

    commitObject = Patients(
        firstName = firstName,
        lastName = lastName,
        password = password,
        dateOfBirth = dateOfBirth
    )
    session_instance.add(commitObject)
    return jsonify({"message": f"added patient with fields {firstName}, {lastName}, {password}, {dateOfBirth}"})

@patients.route("/get", methods=["GET"])
def getPatientByID():
    idPatient = request.json.get("idPatient")
    patientObj = session_instance.query(Patients).filter_by(idPatient=idPatient).first()
    
    if not patientObj:
        return jsonify({"message": f"No patient found with id {idPatient}"})
    
    return jsonify({patientObj.idPatient, patientObj.firstName, patientObj.lastName})