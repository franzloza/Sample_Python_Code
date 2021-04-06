
# Reads a list of numbers and for each number outputs an estimate of
# the running mean, running standard deviation, and running median.
# The input is read from standard in, with one number per line.

# This version allows single entry input in Terminal.
# Numeric entries outputs the calculation.
# Nonnumeric entries quit the program.

import numpy as np

# Enter decimal place accuracy level
accuracyLvl = int(3)

entry_list = []

# Create a single function for desired calculation
# Decimal accuracy level can be customized above.
def statOutput(entry_list, accuracyLvl):
    mean_out = np.round(np.mean(entry_list), accuracyLvl)
    std_out = np.round(np.std(entry_list), accuracyLvl)
    median_out = np.round(np.median(entry_list), accuracyLvl)
    print(f'Mean: {mean_out}, SD: {std_out}, Median: {median_out}')

# Allow float inputs to be added to list.
# The updated list is then plugged into the function.
# Exception closes the program.
while True:
    try:
        inp = float(input("Enter Number: "))
        entry_list.append(float(inp))
        statOutput(entry_list, accuracyLvl)
    except:
        print("Program closed. Enter valid number.")
        break
