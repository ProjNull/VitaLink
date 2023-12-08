from flask import Blueprint, jsonify
from Database.database import Session
patients = Blueprint("Patients_BP", __name__, url_prefix="/patients")

session_instance = Session()