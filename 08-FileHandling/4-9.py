import csv

file_name = 'it_company.csv'

try:
    with open(file_name, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        # Print header
        print("GRAPHIC DESIGNERS")
        print("=================")

        # Loop through each row
        for row in reader:
            # Check if Job Title column contains 'Graphic Designer'
            if row[2] == "Graphic Designer":
                first_name = row[1]
                last_name = row[0]
                email = row[3]
                print(f"{first_name} {last_name},{email}")

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")

