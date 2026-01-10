# Prints file names with extensions of exactly four characters

import re

file_name = 'files.txt'

try:
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()

            # Regex: dot + exactly 4 characters at the end of the line
            pattern = r"\.[a-zA-Z0-9]{4}$"

            if re.search(pattern, line):
                print(line)

except FileNotFoundError:
    print("Error: File not found.")