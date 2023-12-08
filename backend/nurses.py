from flask import Blueprint, jsonify

nurses = Blueprint("Nurses_BP", __name__, url_prefix="/nurses")