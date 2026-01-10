# Counts lines, characters, and words in a text file

try:
    # Read file name from the keyboard
    file_name = input("Enter file name: ")

    # Open the file for reading
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()

    # Count number of lines
    lines = content.splitlines()
    number_of_lines = len(lines)

    # Count number of characters
    number_of_characters = len(content)

    # Count number of words
    words = content.split()
    number_of_words = len(words)

    # Print results
    print(f"File name: {file_name}")
    print(f"Number of lines: {number_of_lines}")
    print(f"Number of characters: {number_of_characters}")
    print(f"Number of words: {number_of_words}")

except FileNotFoundError:
    print("Error: File does not exist.")
