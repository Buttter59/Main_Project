while True:
    import random
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    chose = input("Would you like to roll? (y or n): ")
    if chose == "y":
        print(f"{dice1}, {dice2}")
    elif chose == "n":
        print("Thanks for playing!")
        exit()
    else:
        print("Invalid Choice!")