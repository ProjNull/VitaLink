""" 
    Failed attempts at fixing this code:
    0
    (Increment each time you fail)
"""

from database import Session, func
from flask import Flask, json, jsonify, request, session
from flask_socketio import SocketIO
from exampleModel import Users
from werkzeug.exceptions import HTTPException
from werkzeug.security import check_password_hash, generate_password_hash

SECRET_KEY = "CHANGE-ME-TO-SOMETHING-RANDOM"

api = Flask(__name__)
api.secret_key = SECRET_KEY

socketio = SocketIO(api)
socketio.init_app(api, cors_allowed_origins="*")

if __name__ == "__main__":
    socketio.run(api, debug=True, host="0.0.0.0", port="8002")