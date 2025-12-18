
# RULEBOOK
    # A line of numbers are your battery banks.
    # Pick exactly 2 numbers per line and try to get the highest number possible.
    # You cannot rearrange numbers.
    # If you pick numbers 4 and 7, then your joltage is 47.
    # The sum of all battery banks' joltages should get the escalator working

# GLOBAL VARIABLES
joltage = 0

#banks = """987654321111111
#811111111111119
#234234234234278
#818181911112111"""

#PROCESS

print("Please hold while calculations are performed...")
file = open("Day 3 - Input.txt")

# Split the list into individual banks
for bank in file.readlines():
    bank = bank.strip()

    # For each bank, find the highest digit that is not the last digit.
    # That digit will be the first digit (times ten) of the bank joltage
    largest = 0 # Defines our biggest battery
    largest_index = 0 #What index is the largest battery at?
    for i, battery in enumerate(bank[:-1]):
        if int(battery) > largest:
            largest = int(battery)
            largest_index= i

    # Then find the highest digit after our first digit
    # That will be the second digit
    second_largest = 0 # Defines our second biggest battery
    second_largest_index = 0 #What index is the second largest battery at?
    for battery in bank[largest_index + 1:]:
        if second_largest < int(battery):
            second_largest = int(battery)

    # Add the total joltage to our global value, then process the next bank.
    joltage += (largest*10) + second_largest

#Print total joltage
print(joltage)





