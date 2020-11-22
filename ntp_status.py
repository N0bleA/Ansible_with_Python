import netmiko
import pandas as pd
import time
import argparse
import sys


# This code is to merge all host texts to a single  output file

# Argument parse section to get all text files one by one
parser = argparse.ArgumentParser()
parser.add_argument('switch_list', type=str)
args = parser.parse_args()
switch_list_toList = args.switch_list.split(",")

file2 = open("__PROCESSED_OUTPUT_PYTHON_DIRECTORY__/PYTHON_OUTPUT.txt","w+")

final_output = "" # This is merged text file

# In this loop we iterate all text files and concatanete inside the final_output variable.

for i in range(0,len(switch_list_toList)):
    with open(switch_list_toList[i], 'r') as my_file:
        final_output += my_file.read() + '\n'
        my_file.close()

#print(final_output)

file2.write(final_output) # Write final merged to the PYTHON_OUTPUT.txt.
