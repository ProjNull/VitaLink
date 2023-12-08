""" 
    Failed attempts at fixing this code:
    0
    (Increment each time you fail)
"""

from database import Session, func
from flask import Flask, json, jsonify, request, session
from flask_socketio import SocketIO
from models import Boards
from werkzeug.exceptions import HTTPException
from werkzeug.security import check_password_hash, generate_password_hash

SECRET_KEY = "CHANGE-ME-TO-SOMETHING-RANDOM"

api = Flask(__name__)
api.secret_key = SECRET_KEY