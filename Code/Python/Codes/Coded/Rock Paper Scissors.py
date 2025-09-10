import random

def mechanics():

    random_choice = ("ROCK", "PAPER", "SCISSORS" )
    random_generate = random.choice(random_choice)

    print("Pick form the following\n-ROCK\n-PAPER\n-SCISSORS")
    print("________________________________________________")
    choice = input("Enter your choice: ").upper()
    print("________________________________________________")

    if choice == random_generate:
        print(f"You tied! Enemy python picked {random_generate} :/")

    elif (choice == "ROCK" and random_generate == "SCISSORS") or (choice == "PAPER" and random_generate == "ROCK") or (choice == "SCISSORS" and random_generate == "PAPER"):
        print(f"You won! Python picked {random_generate} :)")
    elif (random_generate == "ROCK" and choice == "SCISSORS") or (random_generate == "PAPER" and choice == "ROCK") or (random_generate == "SCISSORS" and choice == "PAPER"):
        print(f"You lost! Python picked {random_generate} :(")
    else:
        print("Enter correct input")


print("________________________________________________")
print("-----ROCK PAPER SCISSORS-----")
print("________________________________________________")


play = input("Enter would you like to play? Enter Y or N: ").upper()
if play == "Y":
    mechanics()
elif play == "N":
    print("Okay byeee :(")
    exit()
else:
    print("Invalid input. Please enter Y or N")


while True:
    play1 = input("Enter would you like to play again? Enter Y or N: ").upper()
    if play1 == "Y":
        mechanics()
    elif play1 == "N":
        print("Okay byeee :(")
        break
    else:
        print("Invalid input. Please enter Y or N")


print("________________________________________________")
print("Thanks for playing :)")