# Challenge 44, easy
# https://www.reddit.com/r/dailyprogrammer/comments/srowj/4252012_challenge_44_easy/

# Print out sentence with the most words, and number of words in it
# Bonus: print out all words in sentence that are longer than 4 char

import re

text = '''If it will feed nothing else, it will feed my revenge. He hath disgrac'd me and hind'red me half a million; laugh'd at my losses, mock'd at my gains, scorned my nation, thwarted my bargains, cooled my friends, heated mine enemies. And what's his reason? I am a Jew. Hath not a Jew eyes? Hath not a Jew hands, organs, dimensions, senses, affections, passions, fed with the same food, hurt with the same weapons, subject to the same diseases, healed by the same means, warmed and cooled by the same winter and summer, as a Christian is? If you prick us, do we not bleed? If you tickle us, do we not laugh? If you poison us, do we not die? And if you wrong us, shall we not revenge? If we are like you in the rest, we will resemble you in that. If a Jew wrong a Christian, what is his humility? Revenge. If a Christian wrong a Jew, what should his sufferance be by Christian example? Why, revenge. The villainy you teach me I will execute; and it shall go hard but I will better the instruction.'''

sentences = re.split('[.!?]', text)

lengths = []
for i in sentences:
    word_count = len(i.split())
    lengths.append(word_count)

longest_sentence = sentences[lengths.index(max(lengths))]

print(lengths)
print(f"The longest sentence, with {max(lengths)} words, is:")
print("\n", longest_sentence)

longest_list = longest_sentence.split()
more_than_four = []
for word in longest_list:
    word = word.replace(",", "") # strips out commas
    if len(word) > 4:
        more_than_four.append(word)

print("\nThe words in that sentence that are longer than 4 chars are:")
print(more_than_four)
