# Challenge 58, intermediate
# https://www.reddit.com/r/dailyprogrammer/comments/u8jn9/5282012_challenge_58_intermediate/

# Take an input number and return next palindrome
# f(808) = 818
# f(999) = 1001  -- need to take char length increases into account
# f(2133) = 2222
# what is f(3 ^ 39)?
# what is f(7 ^ 100)?

# Basic principle:
# split number up into halves and make palindrome from 1st half
# if new palindrome is <= old number, increase 1st half by 1 and try again
# even-length numbers are trivial
# odd-length numbers: 1st half includes middle char

# Edge cases:
# Increasing char length -- 999 to 1001.

def p(input_number):

    # get front half of number
    if len(str(input_number)) % 2 == 0:        # even-length
        number = str(input_number)
        front_half = number[:int(len(number) / 2)]

        # make palindrome using front_half and check if > number
        new_palindrome = int(front_half + front_half[::-1])
        if new_palindrome <= int(number):
            new_front = str(int(front_half) + 1)

            # check if 99 99 becomes 100 001 instead of 10001
            if len(new_front) > len(str(front_half)):
                newest_palindrome = int(new_front + new_front[::-1][1:])
                return newest_palindrome

            # return simple inverted palindrome
            else:
                newer_palindrome = int(new_front + new_front[::-1])
                return newer_palindrome
        else:
            return new_palindrome

    else:   # odd length version of above
        number = str(input_number)
        front_half = number[:int((len(number) + 1) / 2)]

        new_palindrome = int(front_half + front_half[::-1][1:])
        if new_palindrome <= int(number):
            new_front = str(int(front_half) + 1)

            # check if 999 becomes 100 001 instead of 1001:
            if len(new_front) > len(str(front_half)):
                new_front = new_front[:-1]
                newest_palindrome = int(new_front + new_front[::-1])
                return newest_palindrome
            else:
                newer_palindrome = int(new_front + new_front[::-1][1:])
                return newer_palindrome
        else:
            return new_palindrome

print(p(3 ** 39))
print(p(7 ** 100))
