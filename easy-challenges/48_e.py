# Challenge 48, easy
# https://www.reddit.com/r/dailyprogrammer/comments/t78m8/542012_challenge_48_easy/

def sort_even_odd(input):
    full_list = [int(i) for i in list(input)]

    even_list = []
    odd_list = []

    for i in full_list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    sorted_list = sorted(even_list) + sorted(odd_list)
    sorted_list = [str(i) for i in sorted_list]
    sorted_text = "".join(sorted_list)

    print(sorted_text)

test_list = '68765135468746436546876465321437468'

sort_even_odd(test_list)
