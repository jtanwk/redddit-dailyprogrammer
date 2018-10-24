# Challenge 37, easy
# https://www.reddit.com/r/dailyprogrammer/comments/rzdwq/482012_challenge_37_easy/

def count_lines(doc):
    file = open(doc)
    line_count = 0
    word_count = 0

    for line in file:
        print(line_count, line)
        line_count += 1
        word_count += len(line.split())

    print(f"There are {line_count} lines and {word_count} words in the file.")

count_lines("37_input.txt")
