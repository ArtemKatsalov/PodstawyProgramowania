import json

# Load data from file
with open("euro.json", "r", encoding="utf-8") as file:
    data = json.load(file)

rates = data["rates"]

# Print table header
print("Date            Buying Rate     Selling Rate")
print("=" * 44)

# Print exchange rates
for rate in rates:
    date = rate["effectiveDate"]
    buying = f"{rate['bid']:.4f}"
    selling = f"{rate['ask']:.4f}"

    print(f"{date}      {buying:<14} {selling}")
