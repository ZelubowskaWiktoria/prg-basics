# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.grade = ""

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.grade = 4
    student2.name = "Olivia"
    student2.age = 21
    student2.grade = 3
    student3.name = "Marek"
    student3.age = 23
    student3.grade = 2

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, Final grade: {student1.grade}')
    print(f'{student2.name}, {student2.age} years old, Final grade: {student2.grade}')
    print(f'{student3.name}, {student3.age} years old, Final grade: {student3.grade}')

if __name__ == "__main__":
    main()