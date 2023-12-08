""" 
    Failed attempts at fixing this code:
    1
    (Increment each time you fail)
"""

# Imports libraries
from flask import Flask, json, jsonify, request
from flask_socketio import SocketIO


# Imports files
from Database.patient_models import Patients
from Database.employee_models import Employees
from Database.database import Session, func


# Setup flask instance
SECRET_KEY = "CHANGE-ME-TO-SOMETHING-RANDOM"
session_instance = Session()

app = Flask(__name__)
app.secret_key = SECRET_KEY

socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

# Registering blueprints
from patients import patients
from employee import employee
from admin import admin

app.register_blueprint(patients, url_prefix="/patients")
app.register_blueprint(employee, url_prefix="/employee")
app.register_blueprint(admin, url_prefix="/admin")

# Default routes
# TODO: Add blueprints for better readability
@app.route("/test", methods=["GET","POST"])
def test():
    """
        Handle testing if API works
        
        :return: message: {method} request
    """
    if request.method == "POST":
        return jsonify({"message": "POST request"})
    if request.method == "GET":
        return jsonify({"message": "GET request"})    


if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port="8002")