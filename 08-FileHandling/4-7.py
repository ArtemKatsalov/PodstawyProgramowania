# Counts the number of vowels in text using regular expressions

import re

# Read text from the keyboard
text = input("Enter text: ")

# Regular expression for vowels (both lowercase and uppercase)
pattern = r"[aeiouAEIOU]"

# Find all vowels
vowels = re.findall(pattern, text)

# Print the result
print("Number of vowels:", len(vowels))
