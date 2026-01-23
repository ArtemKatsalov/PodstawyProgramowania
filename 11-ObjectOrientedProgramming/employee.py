class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        # create base text: surname + first letter of name + seniority
        text = f"{self.surname}{self.name[0]}{self.seniority}"

        # check if employee is adult
        if self.age >= 18:
            return text.upper()
        else:
            return text.lower()


# ---- usage ----
emp1 = C("Anna", "May", 17, 7)
emp2 = C("George", "Brown", 21, 4)

print(emp1)
print(emp2)
