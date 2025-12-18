# RULEBOOK
    # 1) Connect two coordinates as opposite corners, and find the largest rectangle possible

# PROCESS
    # 1) Split the lines up into their own coordinate.
    # 2) Compares coordinates against each other.
    # 3) Find the area of the largest rectangle. That is your answer

#STEP 1 - Split coordinates into lines.
sample = open("Day 9 - Input.txt")
sample = sample.readlines()

# GLOBAL VARIABLES
biggest_area = 0

# FUNCTIONS
#Finds the area between two coordinates.
def map_coordinate(line):
    parts = line.split(',')
    x = parts[0]
    y = parts[1]
    return int(x), int(y)

def area_between(a, b):
    x = abs(a[0] - b[0]) + 1
    y = abs(a[1] - b[1]) + 1
    return x * y

# MAIN CODE
#STEP 2 & 3
for i, coordinate in enumerate(map(map_coordinate, sample)):
    for other_coordinate in map(map_coordinate, sample[i + 1:]):
        area = area_between(coordinate, other_coordinate)
        if area > biggest_area:
            biggest_area = area

#GET ANSWER
print(f"\nThe biggest area is << {biggest_area} >> tiles!")