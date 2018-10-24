# Challenge 51, easy
# https://www.reddit.com/r/dailyprogrammer/comments/ti5jc/5112012_challenge_51_easy/

# Inputs: Array A and integer N
# Output: All possible unique combinations of N elements in A
# To check if correct, n-choose-r = (n! / (r!)(n-r)!) combineations

A1 = [1, 2, 3, 4, 5]
N1 = 3

def get_combinations(array, num_items):
    for i in range(1, len(array) - num_items + 2):
        print("i:", i)
        for j in range(i, i + num_items):
            print("j:", j)
            for k in range(i:
                print("k:", k)
                print(i, j, k)

get_combinations(A1, N1)
