
def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login Successful"
    elif username == "":
        return "Username cannot be empty"
    else:
        return "Invalid Credentials"


print(login("admin", "admin123"))

