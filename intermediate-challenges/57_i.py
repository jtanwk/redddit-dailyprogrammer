# Challenge 57, intermediate
# https://www.reddit.com/r/dailyprogrammer/comments/u4mki/5252012_challenge_57_intermediate/

# Only need to iterate over half the make_table, ignoring identity row
# i.e. 0 in row 0, 0 to 1 in row 1, 0 to 2 in row 2, ...
# get indexes and compare to inverted index position
# no need for alphabetical indexes - can strip away letters and use 2D array

prompt = '''ABCDEFGHIJKLMNOPQRST
A11110101111011100010
B10010010000010001100
C01101110010001000000
D10110011001011101100
E10100100011110110100
F01111011000111010010
G00011110001011001110
H01111000010001001000
I01101110010110010011
J00101000100010011110
K10101001100001100000
L01011010011101100110
M10110110010101000100
N10001111101111110010
O11011010010111100110
P01000110111101101000
Q10011001100010100000
R11101011100110110110
S00001100000110010101
T01000110011100101011'''

import re

def count_matches(input_table):
    count = 0

    for row in range(len(input_table)):
        for column in range(row):
            if input_table[row][column] == input_table[column][row] and input_table[row][column] == 1:
                count += 1
            else:
                continue

    return count

def make_table(input_string):
    #takes the prompt, strips the letters and makes it a 2D array
    init_list = input_string.split('\n')
    stripped_array = []

    for i in init_list:
        stripped_string = re.sub(r'[a-zA-Z]', '', i)
        stripped_list = []

        for j in stripped_string:
            stripped_list.append(int(j))

        if len(stripped_list) > 0:
            stripped_array.append(stripped_list)

    return stripped_array

print(count_matches(make_table(prompt)))
