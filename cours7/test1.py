
user_name = input("Enter your User Name: ")
email = input("Enter your Email: ")
password = input("Enter your Password: ")

f2 = open("data.txt", "w+")
f2.write(f"{user_name}\n{email}\n{password}")
f2.close()



