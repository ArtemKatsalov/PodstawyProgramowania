person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}
for key, value in person.items():
    print(f"{key} : {type(value)}")

print(person['name'])
print(person['hobby'])
print(person)
person['surname'] = 'Nowak'
person['marrried'] = False
person['hobby'].append('bicycle')
person['gender'] = 'male'
person['phone']['work'] = '313131444'
print("\nUpdated dictionary contents:")
for key, value in person.items():
    print(f"{key} : {value}")