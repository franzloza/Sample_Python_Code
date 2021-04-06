# Reads a list of numbers and for each number outputs an estimate of
# the running mean, running standard deviation, and running median.
# The input is read from standard in, with one number per line.

# This version allows a file input containing the number entries.

import fileinput
import numpy as np


#Enter decimal place accuracy level
accuracyLvl = int(3)

entry_list = []

# Create a single function for desired calculation
# Decimal accuracy level can be customized above.
def statOutput(entry_list, accuracyLvl):
    mean_out = np.round(np.mean(entry_list), accuracyLvl)
    std_out = np.round(np.std(entry_list), accuracyLvl)
    median_out = np.round(np.median(entry_list), accuracyLvl)
    print(f'Mean: {mean_out}, SD: {std_out}, Median: {median_out}')

# Loop through entries in txt file input to create a list.
# The updated list is then plugged into the function.
# Exception handles nonnumerical errors.
for line in fileinput.input():
    try:
        line = line.strip()
        print(line)
        inp = float(line)
        entry_list.append(inp)
        statOutput(entry_list, accuracyLvl)
    except:
        print("Line entry not allowed")
