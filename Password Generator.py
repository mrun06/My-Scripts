#Create a safe password automatically generated based on the user settings
#Requirements - User will input the password generator parameters (how many characters,
# length of the password, would it include special characters or not, etc)
# - You must avoid characters that could look similar (lower case "L" and number "1" for example
# think of other confusing characters)
# - You should get from the user, how many password should be prompt into the screen.

import random
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '~', '?', '@']

def generate_password(length, nr_uppercase_letters, nr_numbers, nr_symbols):
    password_list = []

    for _ in range(nr_uppercase_letters):
        password_list.append(random.choice(uppercase_letters))

    for _ in range(nr_symbols):
        password_list.append(random.choice(symbols))

    for _ in range(nr_numbers):
        password_list.append(random.choice(numbers))

    remaining_length = length - nr_uppercase_letters - nr_numbers - nr_symbols
    for _ in range(remaining_length):
        password_list.append(random.choice(lowercase_letters))

    random.shuffle(password_list)

    return ''.join(password_list)


def main():
    print("Welcome to the Password Generator!")

    total_length = int(input("How many characters would you like in your password?\n"))
    nr_uppercase_letters = int(input("How many Capital letters would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))

    if nr_uppercase_letters + nr_numbers + nr_symbols > total_length:
        print("The number of characters exceeds the total length! Please try again.")
        return

    num_passwords = int(input("How many password options would you like?\n"))

    print("\nHere are your generated passwords:")
    for i in range(num_passwords):
        password = generate_password(total_length, nr_uppercase_letters, nr_numbers, nr_symbols)
        print(f"Password {i + 1}: {password}")


if __name__ == "__main__":
    main()
