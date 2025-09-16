'''
 11. Strong Password Generator
 Description: Generate a random password ≥12 characters with digits, symbols, upper/lowercase.
Example Input:
 Length: 12
 Expected Output:
 Generated password: A8d!kP3xL$z2
'''

import random
import string

def generate_password():
    length = int(input("Length: "))

    if length < 12:
        print("Password must be at least 12 characters long.")
        return

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars = lowercase + uppercase + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)

    final_password = ''.join(password)
    print("Generated password:", final_password)

def main():
    generate_password()

if __name__ == '__main__':
    main()
