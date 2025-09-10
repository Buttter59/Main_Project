print("")
print("Grade Calculator")
print("")
name = input("Enter your name: ")
print("______________________________________________")
print("")
print(f"Welcome Student: {name}")
print("")
print("______________________________________________")
print("")
ww = int(input("Enter Written Work (30%) Grade:     \t "))
ps = int(input("Enter Performance Task (20%) Grade: \t "))
ex = int(input("Enter Examination  (50%) Grade:     \t"))
print("")
print("______________________________________________")
print("")
ww1 = ww * 0.30
ps1 = ps * 0.20
ex1 = ex * 0.50
ave = ww1 + ps1 + ex1
print(f"{name} your average is {ave}%")
print("")
print("______________________________________________")
print("")
if ave <= 74:
    print("You have a Failing Grade")
elif ave >= 75 and ave <= 89:
    print("Good job you got a Passing Grade")
else:
    print("Amazing You got a High Grade")
print("")
print("______________________________________________")
print("")