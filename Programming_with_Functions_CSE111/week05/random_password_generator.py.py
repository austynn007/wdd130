import random

def generate_password(words):
    password = ''
    for word in words:
        password += word[random.randint(0, len(word) - 1)]  # Select a random character from each word
        password += str(random.randint(0, 9))  # Add a random digit
    return password

words = input("Enter some words (separated by space): ").split()
password = generate_password(words)

print("Your password is:", password)