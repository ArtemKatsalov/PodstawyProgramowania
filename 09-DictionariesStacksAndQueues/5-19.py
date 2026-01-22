import json

# Function to count total number of rooms
def total_rooms(reservations):
    return len(reservations)

# Function to count paid reservations
def count_paid(reservations):
    count = 0
    for r in reservations:
        if r['paid']:
            count += 1
    return count

# Function to count unpaid reservations
def count_unpaid(reservations):
    count = 0
    for r in reservations:
        if not r['paid']:
            count += 1
    return count

# Function to calculate total value of paid reservations
def total_paid_value(reservations):
    total = 0
    for r in reservations:
        if r['paid']:
            total += r['nights'] * r['price_per_night']
    return total

# Function to calculate total value of unpaid reservations
def total_unpaid_value(reservations):
    total = 0
    for r in reservations:
        if not r['paid']:
            total += r['nights'] * r['price_per_night']
    return total

# Main program
with open('reservations.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

reservations = data['reservations']

print("Hotel Reservation Summary")
print("------------------------")
print("Number of rooms:", total_rooms(reservations))
print("Number of paid reservations:", count_paid(reservations))
print("Number of unpaid reservations:", count_unpaid(reservations))
print("Total value of paid reservations: $", total_paid_value(reservations))
print("Total value of unpaid reservations: $", total_unpaid_value(reservations))
