basic_data = {
   "name": "Barbara",
   "age": 21
}

advanced_data = {
   "status": "student",
   "married": False,
   "interest": ["reading", "swimming"]
}

# Create a new dictionary combining the two
person = {}
person.update(basic_data)
person.update(advanced_data)

# Print the contents of the 'person' dictionary
for key, value in person.items():
    print(f"{key} : {value}")
