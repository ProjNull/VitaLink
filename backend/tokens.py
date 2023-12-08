from ast import Dict
from pickle import NONE
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


def generateJWTPacient(firstName: str, lastName: str, idPacient: int):
    # Generates a token for a pacient
    payload = {"firstName": firstName, "lastName": lastName, "idPacient" :idPacient}
    return jwt.encode(payload, secret_key, algorithm="HS256")

def generateJWTEmployee(firstName: str, lastName: str, idEmployee: int, isAdmin: bool):
    # Generates a token for an employee
    payload = {"firstName": firstName, "lastName": lastName, "idEmployee" :idEmployee}
    return jwt.encode(payload, secret_key, algorithm="HS256")

def validateJWT(token: str) -> Dict | None:
    # returns either the decoded token or none if it is invalid
    try:
        return jwt.decode(token, secret_key, algorithms=["HS256"])
    except:
        return None