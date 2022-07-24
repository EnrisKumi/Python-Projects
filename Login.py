user_name = "John"
user_pass = "123456"
attempts = 3

while True:
    un = input("Please enter your username")
    up = input("please enter you password")

    if un!=user_name and up==user_pass:
        print("Wrong username")
        attempts -=1

    elif un==user_name and up!=user_pass:
        print("Wrong password")
        attempts -=1

    elif un!=user_name and up!=user_pass:
        print("Wrong username and password")
        attempts -+1

    else:
        print("logged-in successfully!")
        break

    if attempts == 0:
        print("Error")