import json

# Open the JSON file in read mode with utf-8 encoding
with open('dogs.json', 'r', encoding='utf-8') as file:
    dogs = json.load(file)

print("Dogs younger than 5 years:\n")

for dog in dogs:
    if dog['age'] < 5:
        for key, value in dog.items():
            print(key, ":", value)
        print()  
