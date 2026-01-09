def f(password):
    # check if password has at least 6 characters
    if len(password) < 6:
        return False
    # check if all characters are unique
    return len(password) == len(set(password))
    

# Test examples
print(f("ax15"))       # False, too short
print(f("book123"))    # False, 'o' repeats
print(f("A2water3"))   # True, at least 6 chars, all unique
print(f("qwerty"))     # True, at least 6 chars, all unique
print(f(""))           # False, empty string
