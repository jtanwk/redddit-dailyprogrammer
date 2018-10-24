# Challenge 35, easy
# https://www.reddit.com/r/dailyprogrammer/comments/rr4y2/432012_challenge_35_easy/

# Step 1: find number of lines to print
# Step 2: print n lines in right triangle

import math

def is_triangle_number(test_number):
    '''Returns True if input is a triangle number.'''
    # triangle numbers obey x = n(n+1) / 2
    # so n^2 < 2x < (n+1)^2
    # so n = floor(sqrt(2x))
    index = int(math.floor(math.sqrt(int(test_number) * 2)))
    return int(test_number) % ((index * (index + 1)) / 2) == 0

def get_num_lines(triangle_number):
    '''Gets number of lines to print for triangle number.'''
    return math.floor(math.sqrt(int(triangle_number) * 2))

def print_triangle_line(line_number):
    '''Prints line n in number triangle'''
    end_number = int((line_number * (line_number + 1)) / 2)
    print(*range((end_number - line_number + 1), (end_number + 1)))

def print_triangle(num_lines):
    '''Prints inverse triangle of given number of lines.'''
    for line in range(num_lines, 0, -1):
        print_triangle_line(line)

def attempt(input):
    if is_triangle_number(input):
        print(f"{input} is a triangle number! Printing now:")
        print(print_triangle(get_num_lines(input)))
    else:
        print(f"{input} is not a triangle number.")
        attempt(int(input) - 1)

def main():
    num = input("Enter a number: ")
    attempt(num)

main()
