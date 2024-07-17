Question_9 = """
Write a Python function that generates a random password. The password should contain a mix of uppercase letters, lowercase letters, digits, and special characters.
"""

import random
import string

def generate_random_password(length=12):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters")

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with a mix of all character sets
    all_characters = lowercase + uppercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the list to ensure randomness and then join to form the final password
    random.shuffle(password)
    return ''.join(password)

# Example usage:
print(generate_random_password(12))  # Output: Random 12-character password
print(generate_random_password(16))  # Output: Random 16-character password
