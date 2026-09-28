# #1.Create a class named Circle with an attribute radius. Use a constructor to initialize the radius by accepting input from the user. Define the following methods:
# #
# # getarea() – to calculate and display the area of the circle.
# # getperimeter() – to calculate and display the perimeter (circumference) of the circle.
# #
# # Create an object of the Circle class and call both methods to display the results.
#
# class Circle:
#     def __init__(self):
#         self.radius=int(input('enter the radious : '))
#
#     def getarea(self):
#         area=3.14*self.radius*self.radius
#         print('area= ',area)
#
#     def getperimeter(self):
#         peri=2*3.14*self.radius
#         print('perimeter =',peri)
#
#
# c1=Circle()
# c1.getarea()
# c1.getperimeter()
#
# # 2.Create a class named Account with attributes acctnumber, acctname, and balance. Initialize these values using a constructor by taking input from the user. Define the following methods:
# #
# # withdraw() – to withdraw an amount from the account and update the balance.
# # deposit() – to deposit an amount into the account and update the balance.
# # showbalance() – to display the current balance of the account.
# #
# # Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance.
#
# class Account:
#     def __init__(self):
#         self.acctname=input('enter account name : ')
#         self.acctnumber=int(input('enter the account number : '))
#         self.balance=int(input('enter the account balance : '))
#
#     def withdraw(self):
#         amt=int(input('enter the withdrawel amt :'))
#         if(amount>self.balance):
#             print('insuffient balance')
#         else:
#             self.balance=self.balance-amount
#             self.showbalance()
#
#     def deposite(self):
#         amount=int(input('enter amount : '))
#         self.balance=self.balance+amount
#         self.showbalance()
#
#
#     def showbalance(self):
#         print('current balance ',self.balance)
#
#
#
# a1=Account()
# # a1.withdraw()
# # a1.deposite()
# # a1.showbalance()
#
# a2=Account()
# # a2.withdraw()
# # a.deposite()
# # a1.showbalance()
#
#
# l=[a1,a2]
# for i in l:
#     print(i.acctname)
#     i.showbalance()