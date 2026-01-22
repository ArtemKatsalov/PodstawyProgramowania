hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

# Function that returns a list of hotel names separated by commas
def hotel_list(hotels):
    return ", ".join(hotel["name"] for hotel in hotels)

# Function that returns average price rounded to integer
def avg_price(hotels):
    total = sum(hotel["price"] for hotel in hotels)
    return round(total / len(hotels))

# Print hotel names and average prices
print("Hotels in Krakow:", hotel_list(hotels_in_Krakow))
avg_Krakow = avg_price(hotels_in_Krakow)
print("Average hotel price in Krakow:", avg_Krakow)

print("Hotels in Sopot:", hotel_list(hotels_in_Sopot))
avg_Sopot = avg_price(hotels_in_Sopot)
print("Average hotel price in Sopot:", avg_Sopot)

# Compare which city has cheaper hotels
if avg_Krakow < avg_Sopot:
    print("Cheaper hotels in: Krakow")
elif avg_Sopot < avg_Krakow:
    print("Cheaper hotels in: Sopot")
else:
    print("Hotels have the same average price in both cities")
