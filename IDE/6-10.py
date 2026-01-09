###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"
capitalize = movie.capitalize()
casefold = movie.casefold()
count= movie.count("e")
find= movie.find("Lord")
find2= movie.find("dragon")
# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print( capitalize )

# print title in small letters

print( casefold )

# print how many times the vowel "e" appears in the title
print( count )


# print where in the text is the word "Lord"
print( find )


# print where in the text is the word "dragon"
print( find2 )
