###
# Online store discount calculator
#


num_products = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))

if num_products <= 2:
    total = num_products * product_price
else:
    total = 2 * product_price + (num_products - 2) * product_price * 0.75

print(f"Amount to pay: {total:.2f}")
