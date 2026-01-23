class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
    
    def print_receipt(self):
        print("TAXI RECEIPT")
        print("------------")
        print(f"Distance: {self.distance} km")
        print(f"Rate: €{self.rate_per_km} per km")
        print(f"Total fare: €{self.fare:.2f}")
        print()


def main():
# create two taxi rides
    ride1 = TaxiRide(2)     # €2 per km
    ride2 = TaxiRide(1.5)   # €1.5 per km

    # calculate fares
    ride1.calculate_fare(10)   # 10 km
    ride2.calculate_fare(6)    # 6 km

    # print receipts
    ride1.print_receipt()
    ride2.print_receipt()

    
if __name__ == "__main__":
    main()
