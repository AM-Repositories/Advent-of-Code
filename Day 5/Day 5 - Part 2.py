
# RULEBOOK
    # Using the ranges from our input, figure out how many Fresh IDs are available.

#Process
# 1) Split input into ranges
# 2) compare ranges to check for overlaps
# 3) if overlaps are found, adjust the min/max of the ranges to not overlap
# 4) add adjusted ranges to ranges list
# 5) add the length of the ranges together for a final ID count.

# FUNCTIONS

# GLOBAL VARIABLES
fresh = 0
unique_ranges = []
#MAIN CODE

#STEP 1
file = open("Day 5 - Input.txt")
split_input = file.read()
split_input = split_input.split("\n\n")
ranges, ids = split_input[0], split_input[1]

for r in ranges.splitlines():
    split_range = r.split('-')
    start, end = int(split_range[0]), int(split_range[1])
    #STEP 2 & 3
    for i, (other_start, other_end) in enumerate(unique_ranges):
        if start > other_end or end < other_start:
            continue
        elif start < other_start and end <= other_end:
            end = other_start - 1
        elif start >= other_start and end > other_end:
            start = other_end + 1
        elif start <= other_start and end >= other_end:
            del unique_ranges[i]
        elif start >= other_start and end <= other_end:
            break
    #STEP 4
    else:
        unique_ranges.append((start, end))

#STEP 5
for start, end in set(unique_ranges):
    size = (end - start) + 1
    fresh += size

print(f"\nYou have {fresh} fresh IDs available.")
