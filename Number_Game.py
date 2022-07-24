import random
import  time

print("""

Number Game
Guess the number from 1 tp 100
You have 7 attempts

""")

random_number = random.randint(1,100)
attempts = 7
counter = 0

while True:
    guess = int(input("Enter your guess: "))

    if random_number > guess:
        print("Comparing numbers...")
        time.sleep(1)
        print("Your guess is lower. Try again")
        attempts -= 1
        counter += 1
    elif random_number<guess:
        print("Comparing numbers...")
        time.sleep(1)
        print("Your guess is higher. Try again")
        attempts -= 1
        counter += 1
    else:
        print("Comparing numbers...")
        time.sleep(1)
        print("Your guess is correct!!! ")
        print("You guessed in ", counter , "attemps")
        break
