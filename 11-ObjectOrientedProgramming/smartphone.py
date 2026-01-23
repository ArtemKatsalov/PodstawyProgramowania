class Phone():
    def __init__(self, brand, battery_level, volume_level):
        # States / attributes
        self.brand = brand
        self.battery_level = battery_level
        self.volume_level = volume_level

    # Behaviors / methods
    def make_call(self, number):
        if self.battery_level > 0:
            print(f"Calling {number}...")
            self.battery_level -= 2  # reduce battery for the call
        else:
            print("Battery is empty! Please charge your phone.")

    def charge(self, amount):
        self.battery_level += amount
        if self.battery_level > 100:
            self.battery_level = 100
        print(f"Phone charged. Battery level is now {self.battery_level}%.")

    def adjust_volume(self, level):
        self.volume_level = level
        print(f"Volume set to {self.volume_level}.")

def main():
    my_phone = Phone("Samsung", 85, 10)

    my_phone.make_call("123-456-789")
    my_phone.adjust_volume(15)
    my_phone.charge(10)

    print("\nSmartphone info:")
    print(f"Brand: {my_phone.brand}")
    print(f"Battery level: {my_phone.battery_level}%")
    print(f"Volume level: {my_phone.volume_level}")

if __name__ =="__main__":
    main()