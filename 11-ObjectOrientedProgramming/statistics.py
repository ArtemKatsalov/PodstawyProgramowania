class Statistics:
    def __init__(self):
        # Initialize an empty list to store numbers
        self.numbers = []

    def add_number(self, number):
        # Add a number to the list
        self.numbers.append(number)

    def display_numbers(self):
        # Print all numbers separated by a space
        print("Numbers:", ' '.join(str(num) for num in self.numbers))

    def get_max(self):
        # Return the greatest number
        return max(self.numbers) if self.numbers else None

    def get_min(self):
        # Return the smallest number
        return min(self.numbers) if self.numbers else None

    def get_mean(self):
        # Return the arithmetic mean
        if not self.numbers:
            return None
        return sum(self.numbers) / len(self.numbers)

    def get_median(self):
        # Return the median
        n = len(self.numbers)
        if n == 0:
            return None
        sorted_nums = sorted(self.numbers)
        mid = n // 2
        if n % 2 == 0:
            # If even number of elements, average of the two middle values
            return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
        else:
            # If odd number of elements, middle value
            return sorted_nums[mid]

    def print_statistics(self):
        # Print calculated statistics
        print("Statistics:")
        print("Minimum:", self.get_min())
        print("Maximum:", self.get_max())
        print("Mean:", round(self.get_mean(), 2) if self.numbers else None)
        print("Median:", self.get_median())


# ---- Main program ----
def main():
    stats = Statistics()
    num_count = 5  # how many numbers we want to add

    print(f"Enter {num_count} numbers, pressing Enter after each:")

    for i in range(num_count):
        while True:
            try:
                number = float(input(f"Number {i+1}: "))
                break
            except ValueError:
                print("Invalid input! Please enter a number.")
        stats.add_number(number)  # immediately add the number to the class
        
    # Display numbers and calculated statistics
    stats.display_numbers()
    stats.print_statistics()


if __name__ == "__main__":
    main()
