price = input("Enter price: ")
discount = input("Enter discount %: ")

price = float(price)
discount = float(discount)

discount_amount = price * (discount / 100)
price_with_discount = price - discount_amount

print(f"Price with discount: {price_with_discount:.2f}")
print(f"Reduction: {discount_amount:.2f}")
