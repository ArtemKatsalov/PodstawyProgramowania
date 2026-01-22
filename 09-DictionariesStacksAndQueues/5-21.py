import json

# Create a dictionary describing the favourite movie
data = {
    "favourite_movie": {
        "title": "Inception",
        "year": 2010,
        "director": "Christopher Nolan",
        "genre": ["Sci-Fi", "Action", "Thriller"],
        "rating": 8.8,
        "main_actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"]
    }
}

# Specify the file path and name
file_name = "favourite.json"

# Open the file in write mode and use json.dump() to write the data to the file
with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Data has been written to", file_name)
