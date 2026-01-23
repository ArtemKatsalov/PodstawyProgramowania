# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.hobby = ""

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.hobby = "Swimming"
    student2.name = "Olivia"
    student2.age = 21
    student2.hobby = "Singing"
    student3.name = "Markus"
    student3.age = 20
    student3.hobby = "Drawing"

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, hobby: {student1.hobby}')
    print(f'{student2.name}, {student2.age} years old, hobby: {student2.hobby}')
    print(f'{student3.name}, {student3.age} years old, hobby: {student3.hobby}')

if __name__ == "__main__":
    main()