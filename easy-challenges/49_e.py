# Challenge 49, easy
# https://www.reddit.com/r/dailyprogrammer/comments/tb2h0/572012_challenge_49_easy/

# Simulation of the Monty Hall Problem
# Output: comparison of winning % over n simulations between switching and non

# 1. Pick 1 of 3 doors, none opened
# 2. Host opens another door, with goat
# 3. Choice to switch doors
# 4. Reveal goat or car

import random

def simulate_n_games(num_games):
    switch_games = []
    stay_games = []

    for i in range(num_games):
        switch_games.append(simulate_game(True))
    for i in range(num_games):
        stay_games.append(simulate_game(False))

    print(f"After {num_games} simulations:")
    print("Switch games wins:", sum(switch_games))
    print("Stay games wins:", sum(stay_games))


def simulate_game(switch_choice):
    '''Simulates 1 full round, input switch choice (T/F), output result.'''
    # Step 0: Initialize game
    doors = [0, 0, 0]               # 0 for goat, 1 for car
    opened = [0, 0, 0]              # 0 for closed, 1 for open
    door_car = random.randint(0, 2)
    doors[door_car] = 1             # set car to random door

    # Step 1: Player chooses doors, remains closed
    door_choice_init = random.randint(0, 2)
    goat_doors = [i for i, x in enumerate(doors) if x == 0]

    # Step 2: Host opens goat door
    # If player chose goat door in Step 1, open other goat door, else either one
    if door_choice_init in goat_doors:
        door_to_open = [i for i, x in enumerate(doors) if i != door_choice_init and i != door_car]
        door_to_open = door_to_open[0]
    else:
        door_to_open = goat_doors[random.randint(0, 1)]
    opened[door_to_open] = 1

    # Step 3: Player chooses whether or not to switch doors
    # For simulation, player will switch on odd games, keep on even games.
    if switch_choice == True:
        door_choice_final = [i for i, x in enumerate(opened) if i != door_choice_init and i != door_to_open]
        door_choice_final = door_choice_final[0]
    else:
        door_choice_final = door_choice_init

    # Step 4: Reveal and return results
    if door_choice_final == door_car:
        return 1
    else:
        return 0

simulate_n_games(1000 * 1000)
