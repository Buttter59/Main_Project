#Define your username and password
reg_user = input("Create a username: ")
reg_pass = input("Create a password: ")

#Function to authenticate user
def authenticate():
    print("Login")
    enter_user = input("Enter your username: ")
    enter_pass = input("Enter your password: ")

    if reg_user == enter_user and reg_pass == enter_pass:
        print("Access Granted.")

    else:
        print("Access Denied! Incorrect username or password.")

authenticate()