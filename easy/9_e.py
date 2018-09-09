# Challenge 9, easy
# https://www.reddit.com/r/dailyprogrammer/comments/pu1rf/2172012_challenge_9_easy/

# take digits as input an print in arranged order

digits = input("Enter a number to sort: ")

num_list = [int(x) for x in list(digits)]
num_list.sort()

print(''.join(str(x) for x in num_list))
