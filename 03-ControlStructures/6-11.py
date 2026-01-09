###
# Online store price analyzer
#

previous_price = 200.00
current_price = 140.00

# Calculate percentage decrease
price_change_percent = ((previous_price - current_price) / previous_price) * 100

print(f"Current product price: {current_price:.2f}")
print(f"Previous product price: {previous_price:.2f}")

# Check if price dropped at least 10%
if price_change_percent >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {price_change_percent:.0f}%")
else:
    print("No significant price drop.")
