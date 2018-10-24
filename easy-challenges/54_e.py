# Challenge 54, easy
# https://www.reddit.com/r/dailyprogrammer/comments/tux8f/5192012_challenge_54_easy/

import math
import random

mystring = "The cake is a lie!"
key = 7

def matrix_cypher(input_string, key):
    num_rows = math.ceil(len(input_string) / key)
    num_fill = len(input_string) % key

    # fills empty spaces with random lowercase letters
    fill_letters = []

    for i in range(num_fill):
        rand_letter = chr(math.floor(random.randint(0, 25) + ord('a')))
        fill_letters.append(rand_letter)
    filled_string = input_string + ''.join(fill_letters)
    print(f"Filled string is: {filled_string}")

    # split input string into matrix
    intermediate_list = []

    for i in range(num_rows):
        segment = filled_string[(i * key):((i + 1) * key)]
        intermediate_list.append(segment)
    print(f"String split into matrix is: {intermediate_list}")

    # collect encrypted result and join
    encrypted_list = []

    for i in range(key):
        for j in range(len(intermediate_list)):
            encrypted_list.append(intermediate_list[j][i])

    print(''.join(encrypted_list))

matrix_cypher(mystring, key)
