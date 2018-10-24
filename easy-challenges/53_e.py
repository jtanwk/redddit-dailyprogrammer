# Challenge 53, easy
# https://www.reddit.com/r/dailyprogrammer/comments/tpxq9/5162012_challenge_53_easy/

# take 2 sorted lists and merge efficiently

list1 = [1, 5, 7, 8, 24]
list2 = [2, 3, 4, 7, 9, 13, 27]

# lists are ALREADY sorted
# need to account for lists of unequal lengths

def merge(list1, list2):
    merged_list = []

    while list1 or list2:
        if not list1:
            print(f"list1 is empty, appending {list2[0]} from list2")
            merged_list.append(list2.pop(0))
        elif not list2:
            print(f"list2 is empty, appending {list1[0]} from list1")
            merged_list.append(list1.pop(0))
        elif list1[0] <= list2[0]:
            print(f"{list1[0]} <= {list2[0]}, appending {list1[0]} from list1")
            merged_list.append(list1.pop(0))
        else:
            print(f"{list2[0]} > {list1[0]}, appending {list2[0]} from list2")
            merged_list.append(list2.pop(0))

    print(merged_list)

merge(list1, list2)
