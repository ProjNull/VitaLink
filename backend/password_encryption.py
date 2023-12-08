import bcrypt

def encrypt(password:str)->str:
    toBeHashed = password.encode("utf-8")
    return bcrypt.hashpw(toBeHashed, bcrypt.gensalt())
def checkpw(password:str, hashed:str)->bool:
    return bcrypt.checkpw(password, hashed)