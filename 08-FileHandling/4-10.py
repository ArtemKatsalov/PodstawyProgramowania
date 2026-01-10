import csv

file_name = 'clothing.csv'

try:
    with open(file_name, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        print("Products with price < 60 and stock < 40:")
        print("=======================================")

        for row in reader:
            try:
                price = float(row[5])  
                stock = int(row[6])    

                if price < 60 and stock < 40:
                    print(f"{row[1]} - Price: {price}, Stock: {stock}")
            except ValueError:
                # If row contains text in Price or Stock (like the header), ignore it
                continue

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
