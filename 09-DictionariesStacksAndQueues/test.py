# Create a dictionary
student = {
   'name': 'John',
   'age': 22,
   'major': 'Computer Science'
}

# Accessing a value
print(student['name'])

# Adding a new key-value pair
student['grade'] = 'A'

# Modifying an existing value
student['age'] = 23

# Deleting a key-value pair
del student['major']
print(student)