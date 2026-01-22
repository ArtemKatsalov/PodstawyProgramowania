price_list = {
    'T-shirt': 19.99,
    'Jeans': 49.99,
    'Jacket': 89.99,
    'Sneakers': 59.99,
    'Hat': 15.99
}

#Print products and prices before discount
print("Prices before discount:")
for product, price in price_list.items():
    print(product, price)

#Calculate and print total value before discount
total_before = sum(price_list.values())
print("\nTotal value before discount:", total_before)

#Apply 10% discount
for product in price_list:
    price_list[product] = round(price_list[product] * 0.9, 2)

#Print products and prices after discount
print("\nPrices after 10% discount:")
for product, price in price_list.items():
    print(product, price)

#Calculate and print total value after discount
total_after = sum(price_list.values())
print("\nTotal value after discount:", total_after)
