# Challenge 4, easy
# https://www.reddit.com/r/dailyprogrammer/comments/pm6oj/2122012_challenge_4_easy/

# password generator
# allow user to specify num chars, num passwords to generate
# option to include capitals, numbers, special (!@#%)

import random

print("PASSWORD GENERATOR \n")

print("Setup:")
num_chars = input("How many characters should the password be? ")
capitals = input("Should it include capital letters A-Z? (Y/N) ")
numbers = input("Should it include numerals 0-9? (Y/N) ")
special = input("Should it include special characters \'!@#%\'? (Y/N) ")
num_passwords = input("How many passwords do you want to generate? ")

# create a dictionary to generate password from based on above options
print("\nProcessing...")
small_letters = [chr(i + 97) for i in list(range(26))]
pass_dict = dict(zip(list(range(26)), small_letters))

if capitals == 'Y':
    big_letters = [chr(i + 65) for i in list(range(26))]
    big_numbers = list(range(len(pass_dict), len(pass_dict) + len(big_letters)))
    for i in range(len(big_letters)):
        pass_dict[big_numbers[i]] = big_letters[i]

if numbers == 'Y':
    more_numbers = list(range(len(pass_dict), len(pass_dict) + 10))
    for i in range(10):
        pass_dict[more_numbers[i]] = str(i)

if special == 'Y':
    special_chars = ['!', '@', '#', '%']
    special_numbers = list(range(len(pass_dict), len(pass_dict) + len(special_chars)))
    for i in range(len(special_chars)):
        pass_dict[special_numbers[i]] = special_chars[i]

print(pass_dict)

# generate passwords from above dictionary
print("\nYOUR PASSWORDS:")

for i in range(int(num_passwords)):
    password = []
    for j in range(int(num_chars)):
        rand_char = pass_dict[random.randint(0, len(pass_dict) - 1)]
        password.append(rand_char)
    password = ''.join(password)

    print(f"#{i}: {password}")
