###
# Reads the entire contents of a file
#
def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

# reads the entire file and splits lines into array
file_content = read_from_file('pets.txt')
file_words = file_content.split()

print('The number of words in the text:', len(file_words))