class Student:
    def __init__(self, name, course, year, section):
        self.name = name
        self.course = course
        self.year = year
        self.section = section

    def introduce(self):
        print(f"\tName: {self.name} \n\tCourse: {self.course} \n\tYear: {self.year} \n\tSection: {self.section}")

list_of_students = []

while True:
    nameInput= input("Enter your name: ")
    courseInput = input("Enter your course: ")
    yearInput = str(input("Enter year: "))
    sectionInput = input("Enter your section: ")

    student = Student(nameInput, courseInput, yearInput, sectionInput)
    list_of_students.append(student)

    choice = input("\nDo you want to register another student? [Y/n] ")
    if choice == "Y" or choice == "y":
        continue
    else:
        break

i = 1
for student in list_of_students:
    print(f"\nStudent {i}. ")
    student.introduce()
    i = i + 1