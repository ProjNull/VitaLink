from flask import Blueprint, jsonify

admin = Blueprint("Admin_BP", __name__, url_prefix="/admin")