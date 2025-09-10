# Part 1: Reading the Entire File 

# Create the sample_log.txt file: Open a text editor and paste the example content above into a new file named sample_log.txt. Save it in the same directory where you will save your Python script.
# Write a Python script:
# Open a new Python file (e.g., log_analyzer.py).
# Write code to open sample_log.txt in read mode ('r').
# Read the entire content of the file into a single string variable.
# Print the content of the string variable.
# Ensure you close the file properly using the close() method or a with statement.

text = open("sample_log.txt","r")
content = text.read()
print(content)

text.close()




# Part 2: Reading Line by Line 

# Modify your Python script:
# Open sample_log.txt again in read mode.
# Use a loop to read the file line by line.
# For each line, print the line to the console.
# Explain the difference between reading the entire file at once and reading it line by line in terms of memory usage.

text2 = open("sample_log.txt", "r")

for line in text2:
    print(line.strip())




# Part 3: Extracting Specific Information 

# Further modify your Python script:
# Open sample_log.txt in read mode.
# Iterate through each line of the file.
# For each line, extract the following information using string manipulation techniques (e.g., split()):
# Timestamp
# Event Type
# Description
# Print the extracted information in a formatted way (e.g., "Timestamp: [timestamp], Type: [event_type], Message: [description]").
# Challenge: Count the number of "ERROR" events in the log file.

with open("sample_log.txt", "r") as file:
    for line in file:

        parts = line.split(" - ")
        timestamp = parts[0][1:-1]  
        event_type, description = parts[1].split(": ", 1)  

        print(f"Timestamp: {timestamp}, Type: {event_type}, Message: {description}")

t = "sample_log.txt"
word = "ERROR"
number_words = 0
with open(t, "r") as file:
    for line in file:
        number_words += line.upper().count(word.upper())
print(f"the word {word} appeared {number_words} times in the text file")



# Part 4: Writing to a New File 

# Extend your Python script:
# Create a new file named error_log.txt in write mode ('w').
# Read sample_log.txt line by line.
# If a line contains the word "ERROR", write that entire line to the error_log.txt file.
# After processing all lines, close both files.
# Open error_log.txt and verify that it contains only the error events.
text1 = open("sample_log.txt", "r")
writetext = open("error_log.txt", "w")

for lines in text1:
    diff = lines.split(" - ")
    text = diff[1].split(": ", 1)[0]
    if text == "ERROR":
        writetext.write(lines)

print("Open error_log.txt and verify that it contains only the error events.")
