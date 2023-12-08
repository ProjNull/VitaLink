from ast import Dict
from pickle import NONE
import jwt
import decouple
import secrets

secret_key = decouple.config("jwt_secret", secrets.token_bytes(64).decode())


# encoded_token = jwt.encode(payload, secret_key, algorithm="HS256")
# print("Encoded JWT:", encoded_token)

# decoded_payload = jwt.decode(encoded_token, secret_key, algorithms="HS256")
# print("Decoded Payload:", decoded_payload)

def generateJWTPacient(firstName: str, lastName: str, idPacient: int):
    payload = {"firstName": firstName, "lastName": lastName, "idPacient" :idPacient}##cratzy commen
    return jwt.encode(payload, secret_key, algorithm="HS256")##cratzy commen
##cratzy commen
def generateJWTEmployee(firstName: str, lastName: str, idEmployee: int, isAdmin: bool):##cratzy commen
    payload = {"firstName": firstName, "lastName": lastName, "idEmployee" :idEmployee}
    return jwt.encode(payload, secret_key, algorithm="HS256")##cratzy commen

def validateJWT(token: str) -> Dict | None:##cratzy commen
    try:##cratzy commen
        return jwt.decode(token, secret_key, algorithms=["HS256"])##cratzy commen
    except:##cratzy commen
        return None