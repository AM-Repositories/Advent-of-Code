import math

# RULEBOOK
    # 1) Find the shortest connections between 1,000 junction boxes and fuse them together to make a circuit
    # 2) Other boxes and circuits can be connected if their end pieces are a shortest connection
    # 3) Multiply the sizes of your top three largest circuits for the final answer.

# PROCESS
    # 1) Make a function that checks distances between junctions. - DONE
    # 2) Make a list of our shortest 1,000 connection pairs
    # 3) From that list, form circuit pairs made from those available connections.
    # 4) if two circuits can connect, merge their sets together.
    # 5) After you have 1,000 pairs of junction boxes, multiply the size of our top three circuits.

# EXAMPLE
sample = open("Day 8 - Input.txt")


# FUNCTIONS
def distance_between(a, b):
    x = (a[0] - b[0]) ** 2
    y = (a[1] - b[1]) ** 2
    z = (a[2] - b[2]) ** 2
    return math.sqrt(x + y + z)

def find_smallest_connection(count,boxes):
    connections = []
    for i, junction in enumerate(boxes):
        for other_junction in boxes[i + 1:]:
            distance = distance_between(junction, other_junction)
            connections.append({
                "dist_apart": distance,
                "a": junction,
                "b": other_junction
            })

    connections.sort(key=lambda connection: connection["dist_apart"])
    return connections[:count]

# GLOBAL VARIABLES
boxes = []
circuits = []
top_three = 0


# MAIN CODE - #FROM 1000 CONNECTIONS, MULTIPLY OUR TOP 3 CIRCUITS

#Indexes our coordinates by splitting on the comma, and puts them into a list of tuples.
for line in sample.readlines():
    coords = line.split(',')
    boxes.append((int(coords[0]),int(coords[1]),int(coords[2])))

#
for connection in find_smallest_connection(1000, boxes):
    #Iterates through our junctions to find connections and forms them into circuits, joining circuits if need be.
    a_circuit = None
    try:
        a_circuit = next(circuit for circuit in circuits if connection["a"] in circuit)
    except StopIteration:
        pass
    b_circuit = None
    try:
        b_circuit = next(circuit for circuit in circuits if connection["b"] in circuit)
    except StopIteration:
        pass

    if a_circuit is not None and b_circuit is None:
        a_circuit.add(connection["b"])
    elif a_circuit is None and b_circuit is not None:
        b_circuit.add(connection["a"])
    elif a_circuit is None and b_circuit is None:
        circuits.append({ connection["a"], connection["b"] })
    elif a_circuit == b_circuit:
        continue
    elif a_circuit is not None and b_circuit is not None:
        new_circuit = a_circuit.union(b_circuit)
        circuits.remove(a_circuit)
        circuits.remove(b_circuit)
        circuits.append(new_circuit)
circuits.sort(key=len, reverse=True)

#Print the answer
answer = 1
for size in map(len, circuits[:3]):
    answer *= size
print(answer)
