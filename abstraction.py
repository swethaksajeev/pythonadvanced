#create an abstract class shape with abstract methods get_area() and get_perimeter ()

#create two subclasses
#-rectangle
#=square

#each class should calculate area() amd perimeter () differently
#
# from abc import ABC,abstractmethod
#
# class Shape(ABC):
#
#     @abstractmethod
#     def get_area(self):
#         pass
#
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self):
#         self.length=int(input('enter the length : '))
#         self.breadth=int(input('enter the breadth : '))
#
#     def get_area(self):
#         print('area of rectangle : ',self.length*self.breadth)
#
#     def get_perimeter(self):
#         print('perimeter of rectangle : ', 2*(self.length + self.breadth))
#
#
# class Square(Shape):
#     def __init__(self):
#         self.side = int(input('enter the side : '))
#
#
#     def get_area(self):
#         print('area of square : ', self.side * self.side)
#
#     def get_perimeter(self):
#         print('perimeter of square : ', 4 * self.side)
#
# r=Rectangle()
# r.get_area()
# r.get_perimeter()
# s=Square()
# s.get_area()
# s.get_perimeter()


#create an abstract class Employee witg an abstract method calculate_salary()
#create 2 subclasses
#fulltimeemployee
#parttimeemployee
#each class should calculate salary differently



from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self):
        self.empid = int(input('enter the empid : '))
        self.name = input('enter the name : ')
        self.age = int(input('enter the age : '))


    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.monthly_salary=int(input('enter the monthly salary : '))

    def calculate_salary(self):
        print('empid : ',self.empid,'\nname : ',self.name,'\nage : ',self.age,'\nmonthly salary : ',self.monthly_salary)

class PartTimeEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.workhours = int(input('enter the hours worked : '))
        self.rateperhour=int(input('enter rate per hour : '))

    def calculate_salary(self):
        print('empid : ',self.empid,'\nname : ',self.name,'\nage : ',self.age,'\nwork hours : ',self.workhours,'\nrate per hour : ',self.rateperhour,'\nsalary : ',self.workhours*self.rateperhour)


f=FullTimeEmployee()
f.calculate_salary()
p=PartTimeEmployee()
p.calculate_salary()

