import bcrypt
import jwt
password = "password"
encrypted_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())  # str 객체, bytes로 인코드, salt를 이용하여 암호화
print("password.encode('utf-8') : ",password.encode("utf-8"))
print("bcrypt.gensalt() : ",bcrypt.gensalt())
print("password : ",password)
print("encrypted_password : ",encrypted_password)
# print(encrypted_password)  # bytes-string
print("encrypted_password.decode('utf-8')",encrypted_password.decode("utf-8"))  # str 객체  
print(bcrypt.checkpw(password.encode("utf-8"), encrypted_password))

print(bcrypt.checkpw(password.encode("utf-8"),  b'$2b$12$a1uwlYavYCnCIXl/feukseIvbxBcOrMvtSirBvW3pn5EV44j1RbKi'))
print(bcrypt.checkpw(password.encode("utf-8"), b'$2b$12$47WwccpHKXmc7Z/dXbEiY.2eUkvrh4eCzmPJIm8IMEDJjwuPfT7Cm'))

print(encrypted_password.decode("utf-8"))
temp = encrypted_password.decode("utf-8")
print(temp.encode("utf-8"))

"""
encrypted_password :  b'$2b$12$a1uwlYavYCnCIXl/feukseIvbxBcOrMvtSirBvW3pn5EV44j1RbKi'
encrypted_password.decode('utf-8') $2b$12$a1uwlYavYCnCIXl/feukseIvbxBcOrMvtSirBvW3pn5EV44j1RbKi

encrypted_password :  b'$2b$12$47WwccpHKXmc7Z/dXbEiY.2eUkvrh4eCzmPJIm8IMEDJjwuPfT7Cm'
encrypted_password.decode('utf-8') $2b$12$47WwccpHKXmc7Z/dXbEiY.2eUkvrh4eCzmPJIm8IMEDJjwuPfT7Cm

"""
# json = {
#     "id": "justkode",
#     "password": "password"
# }
# encoded = jwt.encode(json, "secret", algorithm="HS256")  # byte-string
# # decoded = jwt.decode(encoded, "secret", algorithm="HS256")  # dict
# print(encoded)

# decoded = jwt.decode(encoded,"secret",algorithms="HS256")
# print(decoded)
# # print(decoded)