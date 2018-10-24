# Challenge 50, easy
# https://www.reddit.com/r/dailyprogrammer/comments/teua8/592012_challenge_50_easy/

def get_index(credits, grocery_list):
    items = []
    for i in range(len(grocery_list)):
        for j in range(i + 1, len(grocery_list)):
            if grocery_list[i] + grocery_list[j] == credits:
                items.append(i + 1)
                items.append(j + 1)
    print("Credits:", credits)
    print("List:", grocery_list)
    print("Item numbers:", items)
    print("")

C1 = 100
L1 = [5, 75, 25]

C2 = 200
L2 = [150, 24, 79, 50, 88, 345, 3]

C3 = 8
L3 = [2, 1, 9, 4, 4, 56, 90, 3]

get_index(C1, L1)
get_index(C2, L2)
get_index(C3, L3)
