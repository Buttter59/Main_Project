print("_______________________________________________")
name = input("Enter your name: ")
print("Hello, ", name)
noquiz = 5
score = 0
print("_______________________________________________")
ready = input("Are you ready? Enter yes or no: ").lower()
if ready == "yes":
    print("Good, Let's have a quiz.")
elif ready == "no":
    breakpoint
else:
    print("OK.")
print("_______________________________________________")
print("Question No. 1 ")
qui1 = int(input("What is 32 + 21? \t"))
if qui1 == 53:
    print("Nice, Your correct.")
    score += 1
else:
    print("You answered incorrectly.")
print("_______________________________________________")
print("Question No.2 ")
qui2 = int(input("What is 97 - 32? \t"))
if qui2 == 55:
    print("Very Good. Thats correct. ")
    score += 1
else:
    print("You answered incorrectly.")
print("_______________________________________________")
print("Question No.3 ")
qui3 = int(input("What is 14 x 5? \t"))
if qui3 == 70:
    print("Very Nice. Thats correct. ")
    score += 1
else:
    print("You answered incorrectly.")
print("_______________________________________________")
print("Question No.4 ")
qui4 = int(input("What is 320 / 5? \t"))
if qui4 == 64:
    print("Good Job. Thats correct. ")
    score += 1
else:
    print("You answered incorrectly.")
print("_______________________________________________")
print("Question No.5 ")
qui5 = int(input("What is 5 raised to 3? \t"))
if qui5 == 125:
    print("Awesome. Thats correct. ")
    score += 1
else:
    print("You answered incorrectly.")
print("_______________________________________________")
total = float(score/noquiz)*100
print(name, " You got a score of ", total, "%")
if total == 100:
    print("Congrats you got a perfect score.")
elif total >= 90:
    print("Awesome you got an honorable score.")
elif total >= 75:
    print("Good Job, You Passed.")
elif total == 0:
    print("You really need to study.")
else:
    print("Unfortunately you failed, Better luck next time.")
print("_______________________________________________")
