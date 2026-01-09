# Prices of 10 products in the computer store (in currency units)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# Number of units available for each product
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

# Initialize total value
total_value = 0

# Loop through all products and calculate total value
for i in range(len(product_prices)):
    total_value += product_prices[i] * product_quantities[i]

# Print the total value of goods in the store
print(f"Total value of all goods in the store: {total_value:.2f}")
