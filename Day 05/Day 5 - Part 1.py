
# RULEBOOK
    # Using the range of fresh produce, figure out if the ID of the ingredient is fresh or not.
    # If the ID is within the inclusive range, then it's fresh. If not? Spoiled.

#Process
# 1) Split input into fresh ingredient ranges and ingredient IDs
# 2) Check IDs against fresh ranges to see if an ingredient is fresh or spoiled
# 3) If spoiled, move on to next ingredient
# 4) If fresh, Increase fresh ingredient count by 1

# FUNCTIONS

# GLOBAL VARIABLES
fresh = 0
ranges_list = []

#MAIN CODE

#STEP 1
file = open("Day 5 - Input.txt")
split_input = file.read()
split_input = split_input.split("\n\n")
ranges, ids = split_input[0], split_input[1]

for r in ranges.splitlines():
    split_range = r.split('-')
    start, end = int(split_range[0]), int(split_range[1])
    ranges_list.append((start, end))

for id in map(int, ids.splitlines()):
    #STEP 2, 3, and 4
    for (start, end) in ranges_list:
        if start <= id <= end:
            fresh += 1
            break

print(f"\nYou have {fresh} fresh ingredients")
