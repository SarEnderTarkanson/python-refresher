# student ={"name": "Rolf", "grades":(89, 90, 93, 78, 90)}

# def average(sequence):
#     return sum(sequence) / len(sequence)

# print(average(student["grades"]))

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        total = int(sum(self.grades) / len(self.grades))
        return total


student = Student("Bob", (90, 90, 90))

print(student.average_grade())
print(student.name)
print(student.grades)