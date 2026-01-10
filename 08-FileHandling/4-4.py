# Display file in chunks of 5 lines
# and wait for Enter key after each chunk

file_name = 'it_company.csv'

try:
    # Open the file for reading
    with open(file_name, 'r') as file:
        # Read the entire file and split it into lines
        lines = file.read().splitlines()

    index = 0
    total_lines = len(lines)

    # Loop through the file content
    while index < total_lines:
        # Print next 5 lines
        for line in lines[index:index + 5]:
            print(line)

        index += 5

        # Wait for Enter key if there are more lines
        if index < total_lines:
            input("Press Enter key...")

except FileNotFoundError:
    # Handle error when file does not exist
    print(f"Error: File '{file_name}' not found.")

