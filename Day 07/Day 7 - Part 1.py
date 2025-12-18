# RULEBOOK
    # Beams start at the S, and always move down.
    # Once a beam collides with a splitter, it divides into 2 beams.
    # Go until you hit the bottom of the manifold.

# PROCESS
    # 1) Start the beam below the S. Have the beam travel straight down until it hits a splitter.
    # 2) Once a splitter is hit, the beam splits into two on the left and right of the splitter and continues down.
    # 3) Count how many times a splitter is hit, that is your final

file = open("Day 7 - Input.txt")
manifold = file.read()

# FUNCTIONS
def find_splitters(line):
    splits = []
    for i, char in enumerate(line):
        if char == '.':
            continue
        if char == '^':
            splits.append(i)
    return set(splits)

def next_beams(old_beams, splitters):
    new_beams = set()
    splits = 0
    for beam in old_beams:
        # SPLIT BEAM TO LEFT AND RIGHT OF SPLITTER
        if beam in splitters:
            splits += 1
            new_beams.add(beam - 1)
            new_beams.add(beam + 1)
        # IF NO SPLITTER, BEAM DROPS DOWN
        else:
            new_beams.add(beam)
    return splits, new_beams

# GLOBAL VARIABLES
total_splits = 0

# MAIN CODE
beams = set([manifold.splitlines()[0].index("S")])
for line in manifold.splitlines()[1:]:
    # Updates our split and new_beams value, according to what next_beams finds for our beams (old_beams) and splitters (find_splitters).
    splits, new_beams = next_beams(beams, find_splitters(line))
    print(f"'{line}' had {splits} splits: {new_beams}")
    #update beams after this calculation is done to our new beams.
    beams = new_beams
    total_splits += splits

print(f"\n\nYou have {total_splits} total splits!")
