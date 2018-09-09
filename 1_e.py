# Challenge 1, easy
# https://www.reddit.com/r/dailyprogrammer/comments/pih8x/easy_challenge_1/

logfile = open('1_e_output.txt', 'w')

name = input("What is your name? ")
age = input("How old are you in years? ")
username = input("What is your reddit username? ")

logfile.write("Name: " + name + "\n")
logfile.write("Age: " + age + "\n")
logfile.write("Reddit username: " + username + "\n")

print(f"Your name is {name}, you are {age} years old, and your username is {username}.")
