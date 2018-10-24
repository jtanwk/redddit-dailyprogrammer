# Challenge 42, easy
# https://www.reddit.com/r/dailyprogrammer/comments/sobna/4232012_challenge_42_easy/

# BASIC STRUCTURE
# Old MacDonald had a farm, E-I-E-O
# And on his farm he had a cow, E-I-E-I-O
# And a moo moo here, and a moo moo there
# Here a moo, there a moo, everywhere a moo moo
# Old MacDonald had a farm, E-I-E-O

# create a dictionary of animal names and sounds
animals = {
    "cow": "moo",
    "chicken": "cluck",
    "turkey": "gobble",
    "kangaroo": "g'day mate",
    "T-Rex": "GAAAARGH"
}

# print song
for animal in animals:
    print(f'''
    Old MacDonald had a farm, E-I-E-I-O
    And on his farm he had a {animal}, E-I-E-I-O
    And a {animals[animal]} {animals[animal]} here, and a {animals[animal]} {animals[animal]} there
    Here a {animals[animal]}, there a {animals[animal]}, everywhere a {animals[animal]} {animals[animal]}
    Old MacDonald had a farm, E-I-E-I-O
    ''')
