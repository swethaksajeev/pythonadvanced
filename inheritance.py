#single level inheritance

# class Parent:
#     def m1(self):
#         print('in parent class method m1')
#
#     def m2(self):
#         print('in parent class method m2')
#
# # p=Parent()
# # p.m1()
# # p.m2()
#
# class Child(Parent):
#     def m1(self):
#         super().m1()   #super - parent code will work
#         print('in child class method m1')   #method overriding
#     def m3(self):     #own attribute m3()
#         print('in child class method m3')
#
# c=Child()
# c.m1()
# c.m2()
# c.m3()


# class Person:
#     def __init__(self):
#         self.name=input('enter name : ')
#         self.age=int(input('enter age : '))
#     def show(self):
#         print('name : ',self.name,'age: ',self.age)
#
#
#
# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.rollno=int(input('enter roll number : '))
#         self.mark=int(input('enter mark : '))
#
#     def show(self):
#         super().show()
#         print('roll number : ',self.rollno,'mark : ',self.mark)
#
#     def updatemark(self):
#         self.mark=int(input('enter new mark : '))
#
# s=Student()
# s.show()
# s.updatemark()
#
# class Category:
#     def __init__(self):
#         self.category_name=input('enter category name : ')
#
#     def showcategory(self):
#         print('category name is : ',self.category_name)
#
# class Product(Category):
#     def __init__(self):
#         super().__init__()
#         self.product_name=input('enter product name : ')
#         self.price=int(input('enter the price : '))
#         self.quantity=int(input('enter the quantity : '))
#
#     def total_price(self):
#         print('product name : ',self.product_name,'total price : ',self.price * self.quantity,'quantity : ',self.quantity)
#
# p=Product()
# p.showcategory()
# p.total_price()

# class Company:
#     def __init__(self):
#         self.company_name=input('enter company name : ')
#         self.location=input('enter location : ')
#
#     def display_company(self):
#         print('company name : ',self.company_name,'location : ',self.location)
#
# class Employee(Company):
#     def __init__(self):
#         super().__init__()
#         self.empid=int(input('enter empid : '))
#         self.empname=input('enter employee name : ')
#         self.salary=int(input('enter the salary : '))
#
#     def display_details(self):
#         super().display_company()
#         print('empid : ',self.empid,'employee name : ',self.empname,'salary : ',self.salary,'company name : ',self.company_name,'location : ',self.location)
#
#     def update_salary(self):
#         self.salary=self.salary+(self.salary*0.10)
#         print('updated salary : ',self.salary)
#
# e=Employee()
# e.display_details()
# e.update_salary()

#multiple inheritance

# class Hospital:
#     def __init__(self):
#         self.hos_name=input('enter hospital name : ')
#         self.location=input('enter the location : ')
#         self.phone_hos=int(input('enter the phone number : '))
#
#     def display_hospital(self):
#         print('hospital name : ',self.hos_name,'location : ',self.location,'phone number : ',self.phone_hos)
#
# class Department:
#     def __init__(self):
#         self.dept_name=input('enter department name : ')
#         self.doctor_name=input('enter doctor name : ')
#
#     def display_department(self):
#         print('department name : ',self.dept_name,'doctor name : ',self.doctor_name)
#
# class Patient(Hospital,Department):
#     def __init__(self):
#         Hospital.__init__(self)
#         Department.__init__(self)
#         self.patient_name=input('enter patient name : ')
#         self.age=input('enter the age : ')
#         self.gender=input('enter the gender : ')
#         self.phone=int(input('enter the phone number : '))
#         self.admission_date=input('enter the admission date : ')
#         self.bed_no=int(input('enter bed number : '))
#         self.discharge_date=' '
#
#     def set_discharge(self):
#         self.discharge_date=input('enter discharge date :')
#         print('discharge date : ',self.discharge_date)
#
#     def full_summary(self):
#         Hospital.display_hospital(self)
#         Department.display_department(self)
#         print('patient summary \n')
#         print('patient name: ',self.patient_name,'\nage : ',self.age,'\ngender : ',self.gender,'\nphone : ',self.phone,'\nadmission date : ',self.admission_date,'\nbed number : ',self.bed_no)
#         if (self.discharge_date==''):
#             print('not yet discharged')
#         else:
#             print('date of discharged :',self.discharge_date)
#
# p=Patient()
# p.full_summary()
# p.set_discharge()
# p.full_summary()


