from flask import Blueprint, jsonify, request
from Database.employee_models import Employees
from Database.database import Session
import password_encryption as pe

employee = Blueprint("Nurses_BP", __name__, url_prefix="/nurses")

session_instance = Session()

@employee.route("/new", methods=["POST"])
def addEmployee():
    if request.method == "GET": return jsonify({"message": "Only POST enabled"})
       
    
    firstName = request.json.get("firstName")
    lastName = request.json.get("lastName")
    nick = request.json.get("nick")
    password = request.json.get("password")
    email = request.json.get("email")
    dateOfBirth = request.json.get("dateOfBirth")
    isAdmin = request.json.get("isAdmin")
    q = session_instance.query(Employees).filter_by(email=email).first()
     
    if q == email:
        return jsonify({"message": "Someone already has this email!"})
    
    if not firstName or not lastName or not nick or not password or not dateOfBirth or not isAdmin or not email: # TODO: Make list instead
        return jsonify({"message": "No, or incorrect params given!"})
        
        
    commitObject = Employees(
        firstName = firstName,
        lastName = lastName,
        nick = nick,
        password = pe.encrypt(password),
        email = email,
        dateOfBirth = dateOfBirth,
        isAdmin = isAdmin
    )
    session_instance.add(commitObject)
    return jsonify({"message": f"added employee with fields {firstName}, {lastName}, {nick}, {password}, {email}, {dateOfBirth}, {isAdmin}"})


@employee.route("/get", methods=["GET"])
def getEmployee():
    if request.method == "POST": return jsonify({"message": "Only GET enabled"})
    
    idEmployee = request.json.get("idEmployee")
    EmployeeObj = session_instance.query(Employees).filter_by(idEmployee=idEmployee).first()
    
    if not EmployeeObj:
        return jsonify({"message": "Employee not found"})
    
    return jsonify({EmployeeObj})
    
@employee.route("/auth", methods=["GET"])
def authEmployee():
    if request.method == "POST": return jsonify({"Message": "Only GET enabled"}) 
    
    email = request.json.get("email")
    password = request.json.get("password")

    if not password or not email:
        return jsonify({"message": "Missing arguments"})
    
    employeeObj = session_instance.query(Employees).filter_by(email=email).first()
    
    if not employeeObj:
        return jsonify({"message": "Email was not found"})
    
    if not pe.checkpw(password, employeeObj.password):
        return jsonify({"message": "Incorrect password"})
    
    return jsonify("payload.algorithm.signature")

@employee.route("/delete", methods=["DELETE"])
def deleteByID():
    idEmployee = request.json.get("idEmployee")
    
    if not idEmployee:
        return jsonify({"message": "No ID given"})
    
    employeeObj = session_instance.query(Employees).filter_by(idEmployee=idEmployee).first()
    
    session_instance.delete(employeeObj)
    session_instance.commit()
    
    return jsonify({"message": f"Removed employee {employeeObj.firstName}"})