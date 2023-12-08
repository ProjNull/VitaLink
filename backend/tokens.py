import jwt

payload = {"user_id": 123, "username": "john_doe"}
secret_key = "bimbim"

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