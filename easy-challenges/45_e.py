# Challenge 45, easy
# https://www.reddit.com/r/dailyprogrammer/comments/sv6lw/4272012_challenge_45_easy/

# Sample grid
# ----------------
# |    |XXXX|    |
# |    |XXXX|    |
# |XXXX|    |XXXX|
# |XXXX|    |XXXX|
# |    |XXXX|    |
# |    |xxxx|    |
# ----------------

# given dimensions, draws a row of x squares n times
# open_rows draws top line, draw_rows draws two sides and bottom
def draw_grid(nrows, ncols):
    draw_line(int(ncols))
    for i in range(int(nrows)):
        draw_row(int(ncols), i)    # i keeps track of even/odd rows
    draw_line(int(ncols))

def draw_line(ncols):
    grid_length = (int(ncols) * 5) + 1
    print("-" * grid_length)

def draw_row(ncols, row_number):
    if int(row_number) % 2 == 1:        # row is odd-numbered
        draw_odd_row(ncols)
        draw_odd_row(ncols)
    else:                               # row is even-numbered
        draw_even_row(ncols)
        draw_even_row(ncols)

def draw_odd_row(ncols):
    for i in range(int(ncols)):
        if i == 0:
            print("|", " " * 4, "|", sep = "", end = "")
        elif i % 2 == 1:
            print("X" * 4, "|", sep = "", end = "")
        else:
            print(" " * 4, "|", sep = "", end = "")
    print("\n", end = "")

def draw_even_row(ncols):
    for i in range(int(ncols)):
        if i == 0:
            print("|", "X" * 4, "|", sep = "", end = "")
        elif i % 2 == 0:
            print("X" * 4, "|", sep = "", end = "")
        else:
            print(" " * 4, "|", sep = "", end = "")
    print("\n", end = "")

nrows = input("How many rows? ")
ncols = input("How many columns? ")

draw_grid(nrows, ncols)
