import jwt
import decouple
import secrets
import os


def create_jwt_secret():
    data = []
    new_secret = secrets.token_hex(
        127
    )  # No specific reason for 127, I just like the number
    if os.path.exists(".env"):
        with open(".env", "r") as envfile:
            for line in envfile.readlines():
                if line.startswith("jwt_secret="):
                    data.append("jwt_secret=" + new_secret)
                    continue
                data.append(line)
    else:
        data.append('jwt_secret="' + new_secret + '"\n')
    with open(".env", "w") as envfile:
        for line in data:
            envfile.write(line)
        envfile.flush()
    print("WARNING: No JWT secret was specified, so we generated one for you!")


secret_key = decouple.config("jwt_secret", create_jwt_secret())

payload = {"user_id": 123, "username": "john_doe"}

encoded_token = jwt.encode(payload, secret_key, algorithm="HS256")
print("Encoded JWT:", encoded_token)

decoded_payload = jwt.decode(encoded_token, secret_key, algorithms="HS256")
print("Decoded Payload:", decoded_payload)

def generateJWTPacient():
    firstName: str

    lastName: str

    pacientId: int
def generateJWTEmployee():

    firstName: str

    lastName: str

    employeeId: int

    isAdmin: bool
def validateJWT(jwtData) -> dict | None:
    pass