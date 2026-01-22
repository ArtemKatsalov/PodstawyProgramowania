paragraph = "cat dog mouse cat rat cat mouse"

words = paragraph.split()   # split paragraph into words
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print results
for word, count in word_count.items():
    print(word, ":", count)
