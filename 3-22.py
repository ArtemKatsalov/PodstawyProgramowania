import random

# Returns a randomly selected array element
def rand_elem(array):
    index = random.randint(0, len(array) - 1)
    return array[index]

# Example array
numbers = [10, 20, 30, 40, 50]

# Print a few randomly selected elements
print("Random elements:")
print(rand_elem(numbers))
print(rand_elem(numbers))
print(rand_elem(numbers))
