
#RULEBOOK
    # DIGIT IS REPEATING.
    # *AND* DIGIT IS WITHIN RANGE.
    # 11-22, 11 & 22 ARE INVALID, 12-21 ARE VALID.
    # GATHER ALL INVALID IDs AND ADD THEM TOGETHER TO GET ANSWER.

#PROCESS
    # GET LIST OF ALL RANGES
    # FIND INVALID NUMBERS IN EACH RANGE.
    # SUM OF ALL INVALID NUMBERS = ANSWER. (SUM + INVALID NUMBER)

#GLOBAL VARIABLES
sum = 0

print("Please hold while calculations are performed...")
file = open("Day 2 - Input.txt")
for ranch in file.read().split(','):
    split_ranch = ranch.split('-')

    # ITERATE THROUGH THE RANGES, AND CONVERT THEM INTO A STRING
    for num in range(int(split_ranch[0]), int(split_ranch[1]) + 1):
        num = str(num)

        # SKIP ANY NUMBERS THAT ARE ODD (HAVE A "MIDDLE NUMBER")
        if len(num) % 2 != 0:
            # print("---")
            continue

        # SPLIT STRING IN HALF
        first_half = num[int(len(num) / 2):]
        second_half = num[:int(len(num) / 2)]
        # print(f"{first_half},{second_half}")

        # CHECK FOR REPEATS IN RAGE
        if first_half == second_half:
            # Add repeat numbers to global "sum" variable
            print(f"HALVES MATCH:{first_half},{second_half} -- Adding {num} to sum!")
            sum += int(num)

print(f"\nSUM IS: {sum}!")