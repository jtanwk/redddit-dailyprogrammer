# Challenge 46, easy
# https://www.reddit.com/r/dailyprogrammer/comments/szz5y/4302012_challenge_46_easy/

# convert number into binary
# sum all 1s in binary

def get_pop_count(input):
    bin_input = bin(int(input))[2:]
    my_list = list(bin_input)
    my_list = [int(i) for i in my_list]       # list comprehension!
    print(f"{input} in binary is {bin_input}. Its population count is {sum(my_list)}.")

input = input("Enter a number: ")
get_pop_count(input)
