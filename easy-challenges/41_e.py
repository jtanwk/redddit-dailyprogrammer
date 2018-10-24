# Challenge 41, easy
# https://www.reddit.com/r/dailyprogrammer/comments/shp28/4192012_challenge_41_easy/

# limit: 30 char before splitting it up into 2

import math

def open_sentence(sentence):
    width = 30
    if len(sentence) < 30:
        width = len(sentence)

    print("*" * (width + 4))
    print(" " * (width + 4))
    print("*", " " * (width), "*")
    print(" " * (width + 4))

def close_sentence(sentence):
    width = 30
    if len(sentence) < 30:
        width = len(sentence)

    print(" " * (width + 4))
    print("*", " " * (width), "*")
    print(" " * (width + 4))
    print("*" * (width + 4))

def decorate_sentence(sentence):
    print("*", sentence, "*")

def main():
    sentence = input("Enter a sentence: ")

    open_sentence(sentence)
    decorate_sentence(sentence)
    close_sentence(sentence)

main()

## TODO: look up string wrap algorithms
