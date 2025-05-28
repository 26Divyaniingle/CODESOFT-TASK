## password generator


import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password has at least one character from each set
    all_chars = lowercase + uppercase + digits + symbols

    # Generate a password
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to avoid predictable order
    random.shuffle(password)

    return ''.join(password)

def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()