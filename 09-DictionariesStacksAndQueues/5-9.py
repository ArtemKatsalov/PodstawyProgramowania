import csv

# 1. Read province letters and names into a dictionary
province_dict = {}   # key: letter, value: province name
province_count = {}  # key: province name, value: number of vehicles

with open("province.csv", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        letter = row["Letter"]
        name = row["Name"]
        province_dict[letter] = name
        province_count[name] = 0   # initialize count to 0

print(province_dict)
print(province_count)

# 2. Read vehicle registration numbers and count by province
with open("vehicle.txt", encoding="utf-8") as file:
    for line in file:
        reg_number = line.strip()  # remove newline and spaces
        first_letter = reg_number[0]  # first letter indicates province
        if first_letter in province_dict:
            province_name = province_dict[first_letter]
            province_count[province_name] += 1

# 3. Print the results
for province, count in province_count.items():
    print(f"{province}: {count} vehicles")
