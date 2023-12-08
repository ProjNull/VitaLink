import bcrypt

password = b"super secret password"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

if bcrypt.checkpw(password, hashed):
    print("It Matches!")
else:
    print("It Does not Match :(")

# WIP not done
# interface encrypt(password:str)->str checkpw(password:str, hashedpassword:str)->bool