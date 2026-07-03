name ="John"
age = 30
price = 19.99
is_student = True
print("my name is " + name + " and i am " + str(age) + " years old and the price is $" + str(price))
print(name)

print( type(name))
print (type(age))

print (type(price))
print (type(is_student))
name1 = "Bob"
name2 = 'Bob'
name3 = '''Bob'''
print(name1)
print(name2)
print(name3)
age1 = 30
old= False
a=None
print(type (old))
print(type(a))
# print("my name is " + name + " and i am " + str(age) + " years old and the price is $" + str(price))
# print(name)
a = 10
b = 20
# sum = a + b
print(a == b)
print(a -b)
print(a * b)
print(a / b)
print(a % b)
students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")

    student = {
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if len(students) == 0:
        print("No students found.\n")
        return

    print("\nStudent List:")
    print("-" * 40)

    for i, student in enumerate(students, start=1):
        print(f"Student {i}")
        print(f"Name : {student['name']}")
        print(f"Age  : {student['age']}")
        print(f"Grade: {student['grade']}")
        print("-" * 40)


def search_student():
    search_name = input("Enter student name to search: ")

    found = False

    for student in students:
        if student["name"].lower() == search_name.lower():
            print("\nStudent Found:")
            print(f"Name : {student['name']}")
            print(f"Age  : {student['age']}")
            print(f"Grade: {student['grade']}")
            found = True


name ="John"
age = 30
price = 19.99
is_student = True
print("my name is " + name + " and i am " + str(age) + " years old and the price is $" + str(price))
print(name)

print( type(name))
print (type(age))

print (type(price))
print (type(is_student))
name1 = "Bob"
name2 = 'Bob'
name3 = '''Bob'''
print(name1)
print(name2)
print(name3)
age1 = 30
old= False
a=None
print(type (old))
print(type(a))
# print("my name is " + name + " and i am " + str(age) + " years old and the price is $" + str(price))
# print(name)
a = 10
b = 20
# sum = a + b
print(a == b)
print(a -b)
print(a * b)
print(a / b)
print(a % b)
students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")

    student = {
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if len(students) == 0:
        print("No students found.\n")
        return

    print("\nStudent List:")
    print("-" * 40)

    for i, student in enumerate(students, start=1):
        print(f"Student {i}")
        print(f"Name : {student['name']}")
        print(f"Age  : {student['age']}")
        print(f"Grade: {student['grade']}")
        print("-" * 40)


def search_student():
    search_name = input("Enter student name to search: ")

    found = False

    for student in students:
        if student["name"].lower() == search_name.lower():
            print("\nStudent Found:")
            print(f"Name : {student['name']}")
            print(f"Age  : {student['age']}")
            print(f"Grade: {student['grade']}")
            found = True




