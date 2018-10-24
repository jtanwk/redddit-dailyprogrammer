# Challenge 39, easy
# https://www.reddit.com/r/dailyprogrammer/comments/s6bas/4122012_challenge_39_easy/

# program takes input integer n and prints numbers 1 to n, each on a new line
# all numbers divisible by 3 --> Fizz
# all numbers divisible by 5 --> Buzz
# all numbers divisible by both 3 and 5 --> FizzBuzz

def main():
    n = int(input("Enter a number: "))

    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

main()
