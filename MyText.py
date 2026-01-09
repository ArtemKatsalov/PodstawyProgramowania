# MyText module

# Returns the number of words in the text
def word_count(text):
    words = text.split()
    return len(words)


# Returns words ordered from longest to shortest
def words_by_length(text):
    words = text.split()
    n = len(words)

    # simple bubble sort by word length (descending)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(words[j]) < len(words[j + 1]):
                words[j], words[j + 1] = words[j + 1], words[j]

    return words


# Returns words ordered alphabetically
def words_alphabetically(text):
    words = text.split()
    n = len(words)

    # bubble sort alphabetically
    for i in range(n):
        for j in range(0, n - i - 1):
            if words[j] > words[j + 1]:
                words[j], words[j + 1] = words[j + 1], words[j]

    return words
