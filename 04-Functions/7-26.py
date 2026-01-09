def f(text):
    if not text:          # check if text is empty
        return ""
    return "-".join(text) # join all characters with a dash

# Test examples
print(f("Univesity"))  # U-n-i-v-e-r-s-i-t-y
print(f("UE"))         # U-E
print(f("x"))          # x
print(f(""))           # empty string
