from flask import Blueprint, jsonify, request
from middlecrud import (
    get_all_patients,
    get_all_patients_of_nurse,
    allow_access,
    has_access,
    deny_access,
)

admin = Blueprint("Admin_BP", __name__, url_prefix="/admin")


@admin.route("/access/grant", methods=["POST"])
def access_grant():
    patientid = request.json.get("patientid")
    employeeid = request.json.get("employeeid")
    if None in [patientid, employeeid]:
        return {"success": False, "message": "Missing params", "status": 400}
    return {"success": allow_access(patientid, employeeid), "status": 200}


@admin.route("/access/deny", methods=["POST"])
def access_deny():
    patientid = request.json.get("patientid")
    employeeid = request.json.get("employeeid")
    if None in [patientid, employeeid]:
        return {"success": False, "message": "Missing params", "status": 400}
    return {"success": deny_access(patientid, employeeid), "status": 200}


@admin.route("/access/get", methods=["POST"])
def access_get():
    patientid = request.json.get("patientid")
    employeeid = request.json.get("employeeid")
    if None in [patientid, employeeid]:
        return {"success": False, "message": "Missing params", "status": 400}
    return {"success": has_access(patientid, employeeid), "status": 200}


@admin.route("/patients/all")
def patient_list_all():
    return {"patients": get_all_patients()}


@admin.route("/patients/specific")
def patient_list_specific():
    employeeid = request.json.get("employeeid")
    if employeeid is None:
        return {"success": False, "message": "Missing params", "status": 400}
    return {"patients": get_all_patients_of_nurse(employeeid)}
