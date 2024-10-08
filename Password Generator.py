#Create a safe password automatically generated based on the user settings
#Requirements - User will input the password generator parameters (how many characters,
# length of the password, would it include special characters or not, etc)
# - You must avoid characters that could look similar (lower case "L" and number "1" for example
# think of other confusing characters)
# - You should get from the user, how many password should be prompt into the screen.

print("Welcome to the Password Generator!")
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '~', '?', '@']

print("How many characters would you like to have in your password?\n")
print("How many letters would you like?\n")
print("How many numbers would you like?\n")
print("How many symbols would you like?\n")



print("How many password options would you like?\n")