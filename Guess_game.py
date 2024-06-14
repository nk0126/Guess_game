from random import randint

def check_answer():
    answer = randint(1,100)
    level =input("choose your game difficulty level (low, hard) :-").lower()
    if level == "hard":
        attempts = 5
    if level == "low":
        attempts = 10
    #else:
     
     #    attempts = 10
    for i in  range (attempts):

        number = (float(input(f"guess a number from 1 to 100 (Okey Great you have {attempts} attempts left ) :-")))

        attempts -=1

        if number > answer:
            print("It's Too high !!")
        elif number < answer:
            print("It's Too low")
        else:
            print(f"Hurry!! you guess a correct number is {answer}")
            break
    else:

        print ("OPPS Better Luck Next time !!")

        print("*"*40)

        print(f"Sorry you use all attempts & correct Guess is {answer}")

        print("*"*40)

print("*"*40)

print("!! Welcome to Guess Game !!")

print("*"*40)

check_answer()