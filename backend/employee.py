""" 
    Failed attempts at fixing this code:
    0.5
    (Increment each time you fail)
"""

from Database.database import Session
from flask import Blueprint, request
from middlecrud import (delete_employee, get_employee, login_employee, register_employee)

employee = Blueprint("Nurses_BP", __name__, url_prefix="/nurses")

session_instance = Session()


def missing_params(*params):
    return not (None in params)


@employee.route("/new", methods=["POST"])
def addEmployee():
    firstName = request.json.get("firstName")
    lastName = request.json.get("lastName")
    password = request.json.get("password")
    email = request.json.get("email")
    dateOfBirth = request.json.get("dateOfBirth")
    isAdmin = request.json.get("isAdmin", False)
    nick = request.json.get("nick")
    if missing_params(firstName, lastName, password, email, dateOfBirth):
        return {"message": "Missing params!", "status": 400}
    eId = register_employee(
        firstName, lastName, email, password, dateOfBirth, isAdmin, nick
    )
    if not eId:
        return {"message": "Could not register", "status": 500}
    return {"message": f"Employee added", "id": eId, "status": 200}


@employee.route("/get", methods=["GET"])
def getEmployee():
    idEmployee = request.json.get("idEmployee")
    if missing_params(idEmployee):
        return {"message": "Missing idEmployee field in request!", "status": 400}
    e = get_employee(idEmployee)
    if not e:
        return {
            "status": 500,
            "message": "Employee could not be retrieved",
        }
    return {
        "status": 200,
        "employee": e,
        "message": "Employee retrieved",
    }


@employee.route("/auth", methods=["POST"])
def authEmployee():
    email = request.json.get("email")
    password = request.json.get("password")

    if missing_params(email, password):
        return {"message": "Missing arguments", "status": 400}

    if login_employee(email, password):
        return {
            "message": "Logged in!",
            "token": "payload.algorithm.signature",
            "status": 200,
        }
    else:
        return {"message": "Invalid username or password!", "status": 400}


@employee.route("/delete", methods=["DELETE"])
def deleteByID():
    idEmployee = request.json.get("idEmployee")

    if not idEmployee:
        return {"message": "No ID given", "status": 400}

    d = delete_employee(idEmployee)
    if d:
        return {"message": "Employee deleted", "status": 200}
    else:
        return {"message": "An error occoured!", "status": 500}
