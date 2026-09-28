# class Person:
#     def __init__(self,n,a):  #constructor method
#                              #used to initialize object properties
#         self.name=n
#         self.age=a
#
#     def show(self):     #self keyword used to refer current object
#         print(self.name,self.age)
#
# p1=Person('arun',23) #create object p1
#                            #calls __init__ function defined inside Class Person
# p1.show()  #calls show() function
# p2=Person('amal',25) #create object p2
#                            #calls __init__ function defined inside Class Person
# p2.show()


# class Person:
#     def __init__(self):  #constructor method
#                              #used to initialize object properties
#         self.name=input('enter the name :')
#         self.age=int(input('enter the age:'))
#
#     def show(self):     #self keyword used to refer current object
#         print(self.name,self.age)
#
# p1=Person() #create object p1
#                            #calls __init__ function defined inside Class Person
# p1.show()  #calls show() function
# p2=Person() #create object p2
#                            #calls __init__ function defined inside Class Person
# p2.show()
#
# print('enter the print')


#define a class named employee wth attributes empid,name,age,salary,designation and methods getsalary() and showpersonaldetails()
#create objects of employee class and call the methods

# class Employee:
#     def __init__(self):
#         self.empid=int(input('enter empid : '))
#         self.name=input('enter the name : ')
#         self.age=int(input('enter the age : '))
#         self.salary=int(input('enter the salary : '))
#         self.designation=input('enter the designation : ')
#
#     def getsalary(self):
#         print('salary is : ',self.salary)
#
#     def showpersonaldetails(self):
#         print('personal details :',self.empid,self.name,self.age,self.designation)
#
# e1=Employee()
# e1.getsalary()
# e1.showpersonaldetails()
#
# e2=Employee()
# e2.getsalary()
# e2.showpersonaldetails()

#define a class named student with attributes rollno,name,mark1,mark2,mark3 and method display() to display roll number and total mark of a student
#create a student object and call the methods

# class Student:
#     def __init__(self):
#         self.rollno=int(input('enter the roll number : '))
#         self.name=input('enter the name : ')
#         self.mark1=int(input('enter the mark 1 : '))
#         self.mark2=int(input('enter the mark 2 : '))
#         self.mark3=int(input('enter the mark 3 : '))
#
#     def display(self):
#         print('Rollno: ',self.rollno,'Totalmark: ',self.mark1+self.mark2+self.mark3)
#
# s=Student()
# s.display()

#create a class named Book with attributes title,author,price,pages,language and methods
#gettitle(),getauthor(),getprice(),sttitile(),setauthor(),setprice()
#create a book object and call the methods

# class Book:
#     def __init__(self):
#         self.title=input('enter the title : ')
#         self.author=input('enter name of the author : ')
#         self.price=int(input('enter the price : '))
#         self.pages=int(input('enter number of pages : '))
#         self.language=input('enter the language : ')
#
#     def gettitle(self):
#         print('Title: ',self.title)
#
#     def getauthor(self):
#         print('Author: ',self.author)
#
#     def getprice(self):
#         print('price: ',self.price)
#
#     def settitle(self):
#         self.title=input('enter new title : ')
#         self.gettitle()
#
#     def setauthor(self):
#         self.author = input('enter new author : ')
#         self.getauthor()
#
#     def setprice(self):
#         self.price = input('enter new price : ')
#         self.getprice()
#
#     #self.attribute
#     #self.method()
#
# b=Book()
# b.gettitle()
# b.getauthor()
# b.getprice()
#
# #objectname.attributename
# #object
#
# b.settitle()
# b.setprice()
# b.setauthor()

#create a class named Account with attributes acctname,acctname,acctmunber,balance and methods withdraw(),deposite(0,showbalance()
#create an account object and call the methods

class Account:
    def __init__(self):
        self.acctname=input('enter account name : ')
        self.acctnumber=int(input('enter the account number : '))
        self.balance=int(input('enter the account balance : '))

    def withdraw(self):
        amt=int(input('enter the withdrawel amt :'))
        if(amount>self.balance):
            print('insuffient balance')
        else:
            self.balance=self.balance-amount
            self.showbalance()

    def deposite(self):
        amount=int(input('enter amount : '))
        self.balance=self.balance+amount
        self.showbalance()


    def showbalance(self):
        print('current balance ',self.balance)



a1=Account()
# a1.withdraw()
# a1.deposite()
# a1.showbalance()

a2=Account()
# a2.withdraw()
# a2.deposite()
# a2.showbalance()


l=[a1,a2]
for i in l:
    print(i.acctname)
    i.showbalance()