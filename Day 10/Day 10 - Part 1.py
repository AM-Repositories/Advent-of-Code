# RULEBOOK
    # 1) Get the specified switches in the brackets to be in their on positions
    # 2) To toggle a switch, press a button with that index location. Buttons can toggle multiple switches.
    # 3) Figure out how to enable the proper switches in the fewest movements possible.
    # 4) The sum of each problem's "Minimal button press possible" score is your final answer.

# PROCESS
    # 1) Get a set of indicators that are all powered off.
    # 2) Parse out our buttons to apply to indicators.
    # 3) Put the buttons through a logic algorithm to find the shortest route to our answer.
    # 4) Add number of button presses to our global score

# EXAMPLE
sample = open("Day 10 - Input.txt")
sample = sample.readlines()

# GLOBAL VARIABLES
least_presses = 0

# FUNCTIONS
#See how many indicators are within a bracket, and give us a fresh bracket with all the indicators off.
def get_indicators(line):
    lights = line.split("]")[0]
    list_new = []
    list_old = []

    for light in lights[1:]:
        list_new.append(False)
        list_old.append(light == '#')

    return list_new,list_old

#Get a list of our button toggles to be used in our press_buttons function
def get_buttons(line):
    buttons = line.split("] ")[1]
    buttons = buttons.split(" {")[0]

    button_list = []
    for button in buttons.split(' '):
        toggles = []
        for toggle in button[1:-1].split(','):
            toggles.append(int(toggle))
        button_list.append(toggles)
    return button_list

#Press the buttons provided by press button, and invert their boolean.
def press_buttons(indicator, buttons):
    new_indicators = []
    for button in buttons:
        new_indicator = indicator.copy()
        for toggle in button:
            new_indicator[toggle] = not new_indicator[toggle]
        new_indicators.append(new_indicator)
    return new_indicators

#Logic machine that solves our problem in the quickest way possible (Tree method)
def solve_machine(machine):
    start, target = get_indicators(machine)
    indicators = [start]
    buttons = get_buttons(machine)
    press_count = 0
    while target not in indicators:
        press_count += 1
        new_indicators = []
        for indicator in indicators:
            new_indicators += press_buttons(indicator, buttons)
        indicators = new_indicators
    return press_count



# MAIN CODE
print("\nPlease wait while calculations are performed...")

#Solve for each line and add the presses to our total count
for line in sample:
    solve_machine(line)
    least_presses += solve_machine(line)

#GET ANSWER
print(f"\nYou can solve all problems in a total of << {least_presses} >> presses!")