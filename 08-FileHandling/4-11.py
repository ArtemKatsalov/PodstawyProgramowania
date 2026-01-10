# Program to calculate integers, their squares and cubes

# Name of the output file
file_name = 'powers.txt'

with open(file_name, 'w', encoding='utf-8') as file:
    for i in range(1, 101):
        square = i ** 2
        cube = i ** 3
        line = f"{i},{square},{cube}"
        
        file.write(line + '\n')  # save to file

print(f"\nData saved to '{file_name}' successfully.")
