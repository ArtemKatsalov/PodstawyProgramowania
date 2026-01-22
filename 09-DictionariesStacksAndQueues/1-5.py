countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 83240000},
    {"name": "France", "population": 67850000},
    {"name": "Japan", "population": 125800000},
    {"name": "Canada", "population": 39000000}
]

print(f"{'COUNTRY'} {'POPULATION'}")


for country in countries:
    print(f"{country['name']} {country['population']}")
