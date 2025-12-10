
# RULEBOOK
    # Math problems are arranged vertically. Solve them using the operation symbol at the bottom.
    # Sort through the sample input properly, solve all problems, and then sum the totals up.

# PROCESS
    # 1) Take sample and break up the math problems into columns. A new math problem goes into a new row.
    # 2) The operation symbol will go on the last line. Equation should read (a) (symbol) (b) (symbol) (c) (symbol) (d) = answer
    # 3) Solve the problems and add their answers into a total sum.
    # 4) The total sum will be the answer to Day 6

# GLOBAL VARIABLES
answer = 0
total_sum = 0

#MAIN CODE
print("\nPlease hold while calculations are performed...")
file = open("Day 6 - Input.txt")
sample = file.readlines()

op = sample[-1].split()

for i, o in enumerate(op):
    # Indexes the numbers for each equation based on their index position on each linebreak
    a = int(sample[0].split()[i])
    b = int(sample[1].split()[i])
    c = int(sample[2].split()[i])
    d = int(sample[3].split()[i])

    # If we have a multiply operator, our equation does multiplication.
    if o == '*':
        answer = a * b * c * d
        total_sum += answer

    # If we have a multiply operator, our equation does addition.
    if o == '+':
        answer = a + b + c + d
        total_sum += answer

#Print out our total sum / final answer
print(f"\nYour total sum is {total_sum}")

