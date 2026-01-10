import csv

file_name = 'books.txt' 

# Mapping genres to output files
genre_files = {
    "Fantasy": "books_fantasy.txt",
    "Historical": "books_historical.txt",
    "Romance": "books_romance.txt",
    "Classic": "books_classic.txt"
}

try:
    # Open the input file
    with open(file_name, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)  

        for row in reader:
            genre = row[2]  # Genre column
            if genre in genre_files:
                title = row[0]
                author = row[1]
                output_file = genre_files[genre]

                # Open the output file in append mode and write the book
                with open(output_file, 'a', encoding='utf-8') as f:
                    f.write(f"{title},{author}\n")

                print(f"{title},{author}")

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
