def login():
    email = input("Enter Email: ")

    if (email.endswith("@gmail.com")):
        password = input("Enter Password: ")
        if(len(password) <8):
            print("Weak password, Enter Strong Password")
        else:
            print("Successful login")
    elif (email.endswith("@yahoo.com")):
        print("Error in Email Yahoo Email don't support")
    else:
        print("Error in Email don't support")

login()






