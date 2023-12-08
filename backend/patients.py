from flask import Blueprint, jsonify

patients = Blueprint("Patients_BP", __name__, url_prefix="/patients")