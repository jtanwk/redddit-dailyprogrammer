# Challenge 52, easy
# https://www.reddit.com/r/dailyprogrammer/comments/tmnfq/5142012_challenge_52_easy/

word_list = ['Shoe', 'Hat', "ZZTop", "Aa"]

def get_value(word):
    new_letter_values = [ord(letter.upper()) - 64 for letter in word]
    return sum(new_letter_values)

print(sorted(word_list, key = get_value))
