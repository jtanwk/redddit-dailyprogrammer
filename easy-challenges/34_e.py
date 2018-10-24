# Challenge 34, easy
# https://www.reddit.com/r/dailyprogrammer/comments/rmmn8/3312012_challenge_34_easy/

# Inputs: 3 numbers as arguments
# Output: sum of the squares of the 2 larger numbers

def get_two_larger(i, j, k):
    numbers = sorted([i,j,k])
    return (numbers[1] ** 2) + (numbers[2] ** 2)

print(get_two_larger(1,8,7))
