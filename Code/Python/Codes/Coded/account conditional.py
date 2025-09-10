username = "Just123"
password = "Fall123"
reg = input("Are you registered? Enter yes or no: ")
if reg == "yes":
    log = input("Enter username: ")
    log1 = input("Enter password: ")
    if log == username and log1 == password:
        print("You have successfully login ", username)
    else:
        print("Incorrect Username or Password.")
elif reg == "no":
    print("You are unable to login.")
else:
    print("Only answer with yes or no.")