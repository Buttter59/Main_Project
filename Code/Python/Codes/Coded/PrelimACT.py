def get_valid_grade():
    print("______________________________________________________________________")
    print("-----Grade Calculator-----")
    print("______________________________________________________________________")

    prelim = float(input("Enter prelim grade: \t\t"))
    while prelim  < 0 or prelim > 100:
        print("Invalid input. Enter a number between 0 - 100.")
        prelim = float(input("Enter prelim grade: \t\t"))
    mids = float(input("Enter midterm grade: \t\t"))
    while  mids < 0 or  mids > 100:
        print("Invalid input. Enter a number between 0 - 100.")
        mids = float(input("Enter midterm grade: \t\t"))
    semis = float(input("Enter semi-finals grade: \t"))
    while  semis < 0 or  semis > 100:
        print("Invalid input. Enter a number between 0 - 100.")
        semis = float(input("Enter semi-finals grade: \t"))
    finals = float(input("Enter final grade: \t\t"))
    while  finals < 0 or  finals > 100:
        print("Invalid input. Enter a number between 0 - 100.")
        finals = float(input("Enter final grade: \t\t"))
    average = (prelim + mids + semis + finals)/4
    print("______________________________________________________________________")

    print(f"Prelim: \t{prelim}")
    print(f"Midterm: \t{mids}")
    print(f"Semifinals: \t{semis}")
    print(f"Finals: \t{finals}")
    print("______________________________________________________________________")
    print(f"Average Grade: {average}")
    print("______________________________________________________________________")

    if average >= 75:
        print("Status: Passed")
    elif average <= 74:
        print("Status: Failed")
get_valid_grade()   