# Function to get valid grade input from the user
def get_valid_grade():
    while True:
        try:
            grade = input("Enter grade: ")
            
            # Try converting the input to a float to handle numeric input
            grade = float(grade)
            
            # Check if the grade is within the valid range
            if 0 <= grade <= 100:
                return grade
            else:
                print("Error: The grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to calculate the average grade
def calculate_average(grades):
    try:
        if len(grades) == 0:
            raise ZeroDivisionError("Cannot calculate average for an empty list of grades.")
        return sum(grades) / len(grades)
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return 0

# Function to determine the student's status (Pass/Fail)
def determine_status(average_grade):
    if average_grade >= 75:
        return "Passed"
    else:
        return "Failed"

# Main program
def main():
    try:
        # Get grades for prelim, midterm, semifinal, and final
        print("Enter grade for the following:")
        
        prelim = get_valid_grade()
        midterm = get_valid_grade()
        semifinal = get_valid_grade()
        final = get_valid_grade()

        # Create a list of grades and calculate average
        grades = [prelim, midterm, semifinal, final]
        average_grade = calculate_average(grades)

        # Determine status based on average grade
        status = determine_status(average_grade)

        # Display the grades and result
        print(f"Prelim: {prelim}")
        print(f"Midterm: {midterm}")
        print(f"Semifinal: {semifinal}")
        print(f"Finals: {final}")
        print(f"Average Grade: {average_grade:.2f}")
        print(f"Status: {status}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the main function to run the program
if __name__ == "__main__":
    main()