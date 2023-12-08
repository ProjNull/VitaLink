from flask import Blueprint, jsonify, request
from Database.employee_models import Employees
from Database.database import Session

employee = Blueprint("Nurses_BP", __name__, url_prefix="/nurses")

session_instance = Session()

@employee.route("/new", methods=["POST"])
def addEmployee():
    if request.method == "GET":
        return jsonify({"message": "Only POST enabled"})
       
    
    firstName = request.json.get("firstName")
    lastName = request.json.get("lastName")
    nick = request.json.get("nick")
    password = request.json.get("password")
    email = request.json.get("email")
    dateOfBirth = request.json.get("dateOfBirth")
    isAdmin = request.json.get("isAdmin")
    q = session_instance.query(Employees).filter_by(email).first()
     
    if q == email:
        return jsonify({"message": "Someone already has this email!"})
    
    if not firstName or not lastName or not nick or not password or not dateOfBirth or not isAdmin or not email: # TODO: Make list instead
        return jsonify({"message": "No, or incorrect params given!"})
        
        
    commitObject = Employees(
        firstName = firstName,
        lastName = lastName,
        nick = nick,
        password = password,
        email = email,
        dateOfBirth = dateOfBirth,
        isAdmin = isAdmin
    )
    session_instance.add(commitObject)
    return jsonify({"message": f"added employee with fields {firstName}, {lastName}, {nick}, {password}, {email}, {dateOfBirth}, {isAdmin}"})


@employee.route("/get", methods=["GET"])
def getEmployee():
    if request.method == "POST":
        return jsonify({"message": "Only GET enabled"})
    
    idEmployee = request.json.get("idEmployee")
    EmployeeObj = session_instance.query(Employees).filter_by(idEmployee=idEmployee).first()
    
    if not EmployeeObj:
        return jsonify({"message": "Employee not found"})
    
    return jsonify({EmployeeObj})
    