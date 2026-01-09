def f(detector):
    people = 0
    max_people = 0

    for char in detector:
        if char == "+":
            people += 1
        elif char == "-":
            people -= 1
        max_people = max(max_people, people)

    return max_people >= 3
