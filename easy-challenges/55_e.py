# Challenge 55, easy
# https://www.reddit.com/r/dailyprogrammer/comments/txla7/5212012_challenge_55_easy/

# Sliding window minimum problem
# inputs: Array and window size
# output: minimum value of array for each window position

my_array = [4, 3, 2, 1, 5, 7]
my_window = 3

def get_minimum(input_array, window_size):
    min_list = []

    for i in range(len(input_array) - window_size + 1):
        new_window = input_array[i:i + window_size]
        min_list.append(min(new_window))

    print(min_list)

get_minimum(my_array, my_window)
