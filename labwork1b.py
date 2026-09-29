mark = {}
student = []
course = []
def input_student():
    a = int(input("enter the number of students: "))
    for i in range(a):
        b = input("enter the ID,DoB of student: ")
        f = input("enter the name of student: ")
        student.append({"ID,DoB": b, "Name" : f})
def input_course():
    c = int(input("enter the number of course: "))
    for n in range(c):
        d = input("enter the Name of course: ").strip()
        g = input("enter the Id of course: ")
        course.append({"name course": d,"ID":g})
def input_mark():
    e = input("enter the course: ")
    mark[e] = {}
    for stu in student:
        name = student['Name']
        m = float(input(f"enter the mark for {student['Name']}: "))
        mark[e][stu['Name']] = m
def listing_student():
    for stud in student:
        print(f"{stud['Name']},{stud['ID,Dob']}")
def listing_course():
    for cour in course:
        print(f"{cour['name course']},{cour['ID']}")
def listing_mark():
    e = input("enter the course to show mark: ")
    if e in mark:
        for name, score in mark[e].items():
            print(f"{name}: {score}")

input_student()
input_course()
input_mark()

listing_student()
listing_course()
listing_mark()