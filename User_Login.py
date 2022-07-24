user_name = "John"
user_pass = "12345678"

uname = input("Enter your name: ")
upass = input("Enter your password: ")

if uname != user_name and upass == user_pass:
    print("Wrong username")
elif uname == user_name and upass != user_pass:
    print("Wrond password")
elif uname==user_name and upass == user_pass:
    print("Logged in successfully")
else:
    print("Error")
