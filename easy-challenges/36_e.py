# Challenge 36, easy
# https://www.reddit.com/r/dailyprogrammer/comments/ruiob/452012_challenge_36_easy/

# Initialize list of 1000 bits (0 = closed , 1 = open)
# Write function to loop over lockers and toggle based on nth student
# Write function to loop over n students
# Write function to sum number of open lockers at the end.

def toggle(list, locker_number):
    if list[locker_number] == 0:
        list[locker_number] = 1
    elif list[locker_number] == 1:
        list[locker_number] = 0
    else:
        print(f"Error: locker {locker_number} is {list[locker_number]}.")

def toggle_lockers(list, nth_student):
    for i in range(len(list)):
        if (i + 1) % int(nth_student) == 0:
            # print(f"Student #{i + 1} is toggling lockers.")
            toggle(list, i)

def print_open_lockers(list):
    open = []
    for i in range(len(list)):
        if list[i] == 1:
            open.append(i + 1)
    print(open)

lockers = [0] * 1000

for i in range(len(lockers)):
    toggle_lockers(lockers, i + 1)

print(f"After 1000 toggles, there are {sum(lockers)} open lockers.")
print("Open locker numbers:")
print_open_lockers(lockers)
