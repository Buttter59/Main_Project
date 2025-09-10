import random
import string

characters = " " + string.punctuation + string.digits + string.ascii_letters
characters = list(characters)

key =  characters.copy()
random.shuffle(key)

print(f"characters: {characters}")
print(f"key: {key}")


message = input(f"Enter a message to encrypt: ")
encrypted = ""

for letter in message:
    index = characters.index(letter)
    encrypted += key[index]

print(f"original message: {message}")
print(f"encrypted message: {encrypted}")