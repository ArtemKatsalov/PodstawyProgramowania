# Dictionary with products and their quantities
store = {
    'Laptop': 15,
    'Desktop PC': 10,
    'Monitor': 25,
    'Keyboard': 50,
    'Mouse': 60,
    'External Hard Drive': 30,
    'Printer': 12,
    'Router': 20,
    'USB Flash Drive': 100,
    'Graphics Card': 8
}

print("Product  Quantity")

total_products = 0

for product, quantity in store.items():
    print(product, quantity)
    total_products += quantity

print("\nTotal number of products in the store:", total_products)
