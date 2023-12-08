""" 
    Failed attempts at fixing this code:
    0
    (Increment each time you fail)
"""

# Imports libraries
from flask import Flask, json, jsonify, request, session
from flask_socketio import SocketIO


# Imports files
from exampleModel import Users
from database import Session, func


# Setup flask instance
SECRET_KEY = "CHANGE-ME-TO-SOMETHING-RANDOM"

api = Flask(__name__)
api.secret_key = SECRET_KEY

socketio = SocketIO(api)
socketio.init_app(api, cors_allowed_origins="*")


# Default routes
# TODO: Add blueprints for better readability
@api.route("/test", methods=["GET","POST"])
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
    socketio.run(api, debug=True, host="0.0.0.0", port="8002")