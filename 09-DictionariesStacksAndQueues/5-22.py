import json

# Initialize empty dictionary
product = {}

# Read product data from keyboard
product["name"] = input("Enter product name: ")

# Read price as float
product["price"] = float(input("Enter product price: "))

# Read paid status as yes/no and convert to boolean
paid_input = input("Has the product been paid? (yes/no): ")
if paid_input == "yes":
    product["paid"] = True
else:
    product["paid"] = False

# Save product data to JSON file
with open("product.json", "w", encoding="utf-8") as file:
    json.dump(product, file, ensure_ascii=False, indent=4)

print("Product data has been saved to product.json")
