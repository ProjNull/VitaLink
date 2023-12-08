import bcrypt

def hashPassword(password:str)->str:
    toBeHashed = password.encode("utf-8")
    return bcrypt.hashpw(toBeHashed, bcrypt.gensalt())
def checkPassword(password:str, hashed:str)->bool:
    return bcrypt.checkpw(password, hashed)