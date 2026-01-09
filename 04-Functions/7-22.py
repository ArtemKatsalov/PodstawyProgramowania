def f(name):
    # split the text into words
    words = name.split()
    # take the first letter of each word and join them together
    return "".join(word[0] for word in words)


print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))