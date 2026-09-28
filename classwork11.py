# 1.Create a class named Movie with attributes movie name,year,language,director,rating
# and methods display_details() and update_rating()

# class Movie:
#     def __init__(self):
#         self.movie_name=input('enter movie name : ')
#         self.year=int(input('enter year : '))
#         self.language=input('enter language : ')
#         self.director=input('enter director name : ')
#         self.rating=int(input('enter rating (1-5) : '))
#
#     def display_details(self):
#         print('movie name : ',self.movie_name,'\nyear : ',self.year,'\nlanguage : ',self.language,'\ndirector : ',self.director,'\nrating : ',self.rating)
#
#     def update_rating(self):
#         self.rating=int(input('enter new rating : '))
#         print('new rating : ',self.rating)
#
# m=Movie()
# m.display_details()
# m.update_rating()
# m.display_details()



# 2.Create a Python program using Hierarchical Inheritance for a vehicle management system.
#
# Create a parent class Vehicle with the attributes brand, model, color, and year.
# Add a method display() in the Vehicle class to display these details.
# Create two child classes:
# Car with an additional attribute mileage
# Bike with an additional attribute cc
# Override the display() method in both child classes to display the vehicle details along with their respective additional attributes.
# Create objects of both classes, accept input from the user, and display the details.

# class Vehicle:
#     def __init__(self):
#         self.brand=input('enter the brand : ')
#         self.model=input('enter the model : ')
#         self.color=input('enter the color : ')
#         self.year=int(input('enter the year : '))
#
#     def display(self):
#         print('brand : ',self.brand,'\nmodel : ',self.model,'\ncolor : ',self.color,'\nyear : ',self.year)
#
# class Car(Vehicle):
#     def __init__(self):
#         super().__init__()
#         self.mileage=int(input('enter the mileage : '))


#     def display(self):
#         print('Car deatils \n')
#         Vehicle.display(self)
#         print('mileage : ',self.mileage)
#
# class Bike(Vehicle):
#     def __init__(self):
#         super().__init__()
#         self.cc=int(input('enter cc : '))
#
#     def display(self):
#         print('Bike details \n')
#         Vehicle.display(self)
#         print('cc : ',self.cc)
#
# c=Car()
# c.display()
# b=Bike()
# b.display()




