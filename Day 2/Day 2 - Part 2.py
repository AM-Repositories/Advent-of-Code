
#RULEBOOK
    # AN INVALID ID REPEATS AT LEAST TWICE, AND ONLY MADE OF REPEAT DIGITS, AND HAS TO BE WITHIN THE SPECIFIED RANGE
    # 11 & 22 ARE AND INVALID ID. 111 & 999 ARE INVALID AS WELL. 1119 WOULD BE A "VALID" ID AND NOT COUNTED.
    # GATHER ALL INVALID IDs AND ADD THEM TOGETHER TO GET ANSWER.

#PROCESS
    # GET LIST OF ALL RANGES
    # FIND INVALID NUMBERS IN EACH RANGE.
    # SUM OF ALL INVALID NUMBERS = ANSWER. (SUM + INVALID NUMBER)

#GLOBAL VARIABLES
sum = 0

#FUNCTION THAT CHECKS FOR INVALID ID PATTERNS, AND INCREASES THE SUM BY EACH INVALID ID FOUND.
def check_number(num):
        global sum
        num = str(num)

        # ITERATES THROUGH THE VALUE OF AN ID TO CHECK FOR REPEAT PATTERNS OF *ANY* LENGTH
        for character_len in range(1, int(len(num) / 2) + 1):
            # The number of chunks that match the first chunk
            num_of_matches = 1
            patterns = range(character_len, len(num), character_len)
            # Iterate through chunks to see if all patterns are identical.
            for pattern_num in patterns:
                first_chunk = num[:character_len]
                chunk_to_check = num[pattern_num:character_len + pattern_num]
                if first_chunk == chunk_to_check:
                    num_of_matches += 1

            # INCREASE SUM COUNT BY VERIFIED INVALID IDs
            if num_of_matches * character_len == len(num):
                #print(f"Found invalid id: {num}")
                sum += int(num)
                return

# SPLIT OUR STRING INTO INTEGERS, AND THEN APPLY OUR PATTERN FUNCTION TO EACH ITERATION.
print("\nPlease hold while calculations are performed.")
file = open("Day 2 - Input.txt")
for ranch in file.read().split(','):
    split_ranch = ranch.split('-')
    for num in range(int(split_ranch[0]), int(split_ranch[1]) + 1):
        check_number(num)

print(f"\nSUM IS: {sum}!")
