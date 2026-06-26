student = {}


while True:
    print("\n-----STUDENT MANAGER APP-----")
    print("1. Add Student")
    print("2. View Students")
    print("3. check Student")
    print("4. Exit")

    choice = input("Enter your choice : ")
    
    # add student

    if choice == "1":
        name = input("Enter student name: ")
        marks = marks = (input("Enter student marks: "))
        student[name] = marks

        print(f"Student {name} added successfully!")

        # view students
        
    elif choice == "2":
            if not student:
                print("No students found.")
            else:
                 for name, marks in student.items():
                      print(name, ":", marks)

    # check result 

    elif choice == "3":
        name = input("Enter student name to check result: ")
        if name in student:
            marks = student[name]
            """"
            aaaa : 44
            aaaa
            """