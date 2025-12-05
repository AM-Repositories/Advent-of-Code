
# RULEBOOK
    # A line of numbers are your battery banks.
    # Pick exactly 12 numbers per line and try to get the highest number possible.
    # You cannot rearrange numbers.
    # If you pick numbers 4, 5, 7, 3, then your joltage is 4,573.
    # The sum of all battery banks' joltages should HOPEFULLY get the escalator working

# GLOBAL VARIABLES
joltage = 0

#Reads our input file
print("Please hold while calculations are performed...")
file = open("Day 3 - Input.txt")

#PROCESS

#Function that finds the largest battery, referencing our bank.
def largest_battery(bank):
        # For each bank, find the highest digit that is not the last digit.
        # That digit will be the first digit (times ten) of the bank joltage
        largest = 0 # Defines our biggest battery
        largest_index = 0 #What index is the largest battery at?
        for i, battery in enumerate(bank):
            if int(battery) > largest:
                largest = int(battery)
                largest_index= i

        return largest_index, largest

# For loop that iterates through our list of banks to find the highest joltage combination
for bank in file.readlines():
    bank = bank.strip()
    # Default values for our battery number, and what index we start on per loop
    battery = 0
    start = 0
    #Set a range that decreases every run.
    for num in range(0, 12):
        power = 11 - num
        end = len(bank) - power

        # Add the total joltage to our global value, then process the next bank.
        i, digit = largest_battery(bank[start:end])

        #Update our start value so that we don't pick the same number again.
        start = i + start + 1

        #Updates our battery value according to index location in the joltage.
        battery += digit * (10 ** power)

    #Add battery to total joltage count, and loop again.
    joltage += battery
#Print total joltage
print(f"\nTotal Joltage: {joltage}")