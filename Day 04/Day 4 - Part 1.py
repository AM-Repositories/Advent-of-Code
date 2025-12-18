
# RULEBOOK
    # Figure out how many rolls of paper can be accessed/moved by a forklift
    # A paper roll (@) can only be accessed if there are FEWER than 4 (1-3) rolls of paper around it (in a 3x3)

print("Please hold while calculations are performed...")
file = open("Day 4 - Input.txt")


#Process
# 1) Create shelves from our sample, and iterate individual cells by its column and row position.
# 2) Check and see if the space is paper (@). If so, move on to step 3. If not, move to next space and repeat this step.
# 3) Form a 3x3 square with the selected paper roll in the center.
# 4) Check the surrounding spaces for other paper rolls.
# 5) If there are MORE than 3 paper rolls, roll is INVALID, move to next space, and repeat step 2
# 6) If there are LESS than 3 paper rolls, mare as VALID, move to next space, and repeat step 2.

# FUNCTIONS
# Checks to see if the selected space is a paper roll
def is_paper(paper):
    if paper == '@':
        return True
    else:
        return False
        # MOVE ON YOU STINKY LIL THING

def adjacent_cells(row, col):
    # Row left and right
    yield row, col - 1
    yield row, col + 1

    # Rows below
    yield row + 1, col + 1
    yield row + 1, col
    yield row + 1, col - 1

    # Rows above
    yield row - 1, col + 1
    yield row - 1, col
    yield row - 1, col - 1

# GLOBAL VARIABLES
accessible_rolls = 0

#MAIN CODE

#STEP 1
shelves = file.readlines()
#Set the row length
for row in range(0, len(shelves)):
    #Set the column, according to which row we're on
    for col in range(0, len(shelves[row])):
        paper = shelves[row][col]
        #STEP 2
        if is_paper(paper):
            #STEP 3 & 4
            surrounding_rolls = 0
            for r, c in adjacent_cells(row, col):
                if r < 0 or c < 0:
                    continue
                try:
                    if shelves[r][c] == '@':
                        surrounding_rolls += 1
                except IndexError:
                    continue

            # STEP 5 & 6
            if surrounding_rolls < 4:
                accessible_rolls += 1


print(accessible_rolls)