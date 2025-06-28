# class student:
#     name=None
#     m1=None
#     m2=None
#     m3=None
#
#     def tot(self):
#         return self.m1 + self.m2 + self.m3
#
# s1=student()
# s1.name= 'aswath'
# s1.m1=23
# s1.m2=12
# s1.m3=3
#
# s2=student()
# s2.name='pavi'
# s2.m1=33
# s2.m2=22
# s2.m3=12
#
# if s1.tot() > s2.tot():
#     print("aswath mass")
# else:
#     print("pavi mass")





class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def tot(self):
        return self.m1 + self.m2 + self.m3

# Create a list of 10 students
students = [
    Student('aswath', 23, 12, 3),
    Student('pavi', 33, 22, 12),
    Student('mani', 45, 34, 23),
    Student('divya', 32, 25, 27),
    Student('ravi', 29, 31, 25),
    Student('kiran', 30, 28, 30),
    Student('lakshmi', 26, 22, 20),
    Student('john', 38, 40, 39),
    Student('sara', 34, 35, 36),
    Student('deepa', 41, 42, 43)
]

# Find student with highest total
top_student = students[0]
for student in students[1:]:
    if student.tot() > top_student.tot():
        top_student = student

print(f"The top student is {top_student.name} with total marks {top_student.tot()}.")
