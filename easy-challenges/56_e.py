# Challenge 56, easy
# https://www.reddit.com/r/dailyprogrammer/comments/u0tdt/5232012_challenge_56_easy/

# 1 a
# 2 a b a
# 3 aba c aba
# 4 abacaba d abacaba

# n abacaba(n-1) [nth letter] abacaba(n-1)

from time import perf_counter

start = perf_counter()

def abacaba(num):
    if num == 1:
        return 'a'
    else:
        prev_num = abacaba(num - 1)
        return prev_num + chr(num + 96) + prev_num

print(abacaba(26))
print("done in:", perf_counter() - start, "seconds")
