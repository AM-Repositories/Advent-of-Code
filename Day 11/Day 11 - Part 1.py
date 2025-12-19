# RULEBOOK
    # 1) You are given a device labelled "You" that has 1+ outputs that connects to other devices with 1+ outputs.
    # 2) Your goal is to route yourself from "You" to "Out" by connecting devices together.
    # 3) The final answer is the number of possible routes you can take to get from "You" to "Out."

# PROCESS
    # 1) Parse out our input into a dictionary of devices and their connections.
    # 2) Use a recursive function to find potential paths to "out"
    # 3) Once an "out" path is found, increase potential path count by 1

# INPUT
sample = open("Day 11 - Input.txt")
sample = sample.read()

# FUNCTIONS
def parse_device(line):
    devices = line.split(': ')
    connected = []
    for connection in devices[1].split():
        connected.append(connection)

    return devices[0], connected

def parse(input):
    devices = {}
    for line in input.splitlines():
        device, connected = parse_device(line)
        devices[device] = connected
    return devices

def path_seeker(current, devices):
    if current.lower() == "out":
        return 1
    total = 0
    connected = devices[current]
    for other in connected:
        total += path_seeker(other, devices)
    return total

# MAIN CODE
rack = parse(sample)
print(f"\nThere are {path_seeker("you", rack)} possible routes to 'out'")

