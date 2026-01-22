import json

filename = "voting.json"

# 1. Read the contents of the json file
try:
    with open(filename, "r", encoding="utf-8") as file:
        votes = json.load(file)
except FileNotFoundError:
    votes = {}  # if the file does not exist, create an empty dictionary

# 2. Vote for a person
person_name = input("Name of the person you are voting for: ")

if person_name in votes:
    votes[person_name] += 1
else:
    votes[person_name] = 1

# 3. Save voting data to json file
with open(filename, "w", encoding="utf-8") as file:
    json.dump(votes, file, ensure_ascii=False, indent=4)

print(f"Vote recorded for {person_name}.")
