# Write a menu-driven Python program using a class Student to perform the following operations:

# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.


l = []

class Student():
    def __init__(self):
        self.rollno = int(input("enter roll no : "))
        self.stuname = input("enter student name : ")
        self.marks = int(input("enter marks : "))

    def updatemark(self):
        self.marks = int(input("enter new marks : "))
        print("updated mark = ", self.marks)

    def display(self):
        print("Roll No:", self.rollno, "Name:", self.stuname, "Marks:", self.marks)


while(True):
    print("\n1.Add Student\n2.Update Marks\n3.Display All Student Details\n4.Search Student by Roll Number\n5.Delete Student\n6.Exit")
    ch = int(input("enter your choice (1-6) : "))

    if ch == 1:
        a = Student()
        l.append(a)
        print("Student added successfully!")

    elif ch == 2:
        number = int(input("enter roll no to update : "))
        for i in l:
            if i.rollno == number:
                i.updatemark()
                break
        else:
            print("student does not exist")

    elif ch == 3:
        if len(l) == 0:
            print("No student records found")
        for i in l:
            i.display()

    elif ch == 4:
        number = int(input("enter roll no to search : "))
        for i in l:
            if i.rollno == number:
                i.display()
                break
        else:
            print("roll number does not exist")

    elif ch == 5:
        number = int(input("enter roll no to delete : "))
        for i in l:
            if i.rollno == number:
                l.remove(i)
                print("Student deleted successfully!")
                break
        else:
            print("student does not exist")

    elif ch == 6:
        print(".....exit.....")
        break 