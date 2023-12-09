from Database.database import Base, engine
from flask import Flask, request, send_file
from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

from admin import admin
from employee import employee
from patients import patients
from messages import messages

Base.metadata.create_all(engine)

app.register_blueprint(patients, url_prefix="/patients")
app.register_blueprint(employee, url_prefix="/employee")
app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(messages, url_prefix="/messages")

@app.route("/", methods=["GET", "POST"])
def root():
    """
    Serves as a test to see if the server lives.
    Returns "POST request" if access through post
    Returns "GET request" if accessed through get
    """
    return {"message": request.method + " request", "status": 200}

from io import BytesIO
import qrcode

@app.route("/genqr")
def generate_qr_code():
    # Data to encode in the QR code
    data_to_encode = request.args.get(
        "data", "Default Data - No data received")

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data_to_encode)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    img_buffer = BytesIO()

    # Save the image to the buffer
    img.save(img_buffer)
    img_buffer.seek(0)

    # Serve the image from the buffer
    return send_file(img_buffer, mimetype="image/png")

if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port="8002")
