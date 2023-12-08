""" 
    Failed attempts at fixing this code:
    2
    Successfull attempts:
    1
    (Increment each time you fail)
"""

from Database.database import Base, engine

# Imports libraries
from flask import Flask, request
from flask_socketio import SocketIO

Base.metadata.create_all(engine)


app = Flask(__name__)

socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

from admin import admin
from employee import employee
# Registering blueprints
from patients import patients

app.register_blueprint(patients, url_prefix="/patients")
app.register_blueprint(employee, url_prefix="/employee")
app.register_blueprint(admin, url_prefix="/admin")


@app.route("/", methods=["GET", "POST"])
def test():
    """
    Handle testing if API works

    :return: message: {method} request
    """
    return {"message": request.method + " request", "status": 200}


if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port="8002")
