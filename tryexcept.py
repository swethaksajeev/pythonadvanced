#
# # 1.file read
# # 2.file write
# # 3.file append
# # 4.file search
# # 5.file delete
# # 6exit
#
# def file_read():
#     try:
#         filename = input('enter file name : ')
#         f=open(filename, 'r')
#         s=f.read()
#         print(s)
#         f.close()
#     except:
#         print('File does not exist')
# def file_write():
#     filename=input('enter filename: ')
#     f1=open(filename,'w')
#     g=input('enter content : ')
#     f1.write(g)
#     print('content successfully written')
#     f1.close()
#
# def file_append():
#     filename = input('enter filename: ')
#     f2 = open(filename, 'a')
#     content=input('enter content : ')
#     f2.write(content)
#     print('successfully appended')
#     f2.close()
#
#
# def file_search():
#     filename = input('enter filename: ')
#     f=open(filename,'r')
#     s=f.read()
#     word=input('enter the word to search')
#     if word in s:
#         print('word',word,'is present')
#
#     else:
#         print('word', word, 'is not present')
#     f.close()
# def file_delete():
#     import os
#     d=input('enter file to be deleted : ')
#     os.remove(d)
#     print('file deleted')
#
# while(True):
#     print('Menu Driven-File Operation')
#     print('1.File Read')
#     print('2.File Write')
#     print('3.File Append')
#     print('4.File Search')
#     print('5.File Delete')
#     print('6.Exit')
#
#     ch=int(input('enter the choice: '))
#     if ch==1:
#         file_read()
#     elif ch==2:
#         file_write()
#     elif ch==3:
#         file_append()
#     elif ch==4:
#         file_search()
#     elif ch==5:
#         file_delete()
#     else:
#         exit()
import math

# try:
#     n1=int(input('enter n1'))
#     n2=int(input('enter n2'))
#
#     r=n1/n2
#
# except ValueError:
#     print('ValueError')
#
# except ZeroDivisionError:
#     print('ZeroDivisionError')
#
# except:
#     print('error')
#
# else:
#     print('result', r)
#
#
# finally:
#     print('done')


# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input

# import math
# while(True):
#     try:
#         num=int(input('enter the number : '))
#         fact=math.factorial(num)
#         print(fact)
#         break
#     except ValueError:
#         print('ValueError is there')

# or

# def fact():
#     try:
#             num = int(input('enter the number : '))
#             f= math.factorial(num)
#             print(f)
#
#     except :
#             print('ValueError is there')
#             fact() #recursion function - a function that calls itself
#     else:
#             pass
#
# fact()


# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.

# try:
#     n1=int(input('enter n1 : '))
#     n2=int(input('enter n2 : '))
#     op=input('enter operator : ')
#     if op=="+":
#         print('num1+num2 = ',n1+n2)
#
#     elif op=='-':
#         print('num1-num2 = ', n1 - n2)
#
#     elif op=='*':
#         print('num1*num2 = ', n1 * n2)
#
#     elif op=='/':
#         print('num1/num2 = ', n1 / n2)
#
# except ZeroDivisionError:
#     print('ZeroDivisionError')
#
# except ValueError:
#     print('Invalid Input')
# except:
#     print('error')


#or


# while True:
#     try:
#         print('1.Addition')
#         print('2.Subtraction')
#         print('3.multiplication')
#         print('4.Division')
#         print('5.exit')
#
#         n = int(input("Enter choice"))
#         if n in [1,2,3,4]:
#             n1 = int(input("Enter number"))
#             n2 = int(input("Enter number"))
#
#             s=n1+n2
#             d=n1-n2
#             m=n1*n2
#             q=n1/n2
#     except ZeroDivisionError:
#         print("Zero Division Error")
#     except ValueError:
#         print("Invalid Input")
#     except:
#         print("Error")
#     else:
#
#         if n == 1:
#                 print('Result', s)
#         elif n == 2:
#                 print("Result", d)
#         elif n == 3:
#                 print("Result", m)
#         elif n == 4:
#                 print("Result", q)
#         else:
#             exit()

# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist

# try:
#     n=input('enter file to open : ')
#     f=open(n,'r')
#     s=f.read()
# except FileNotFoundError:
#     print('file not exist')
#
# else:
#     print(s)
#     f.close()


#Given a Dictionary
#
# d={"name':"arun","age":23,"place":"ekm"}
# Write a program to ask the user to enter a key and display its value.
# Handle KeyError if key does not exist

# try:
#     d={'name':'arun','age':23,'place':'ekm'}
#     key=input('enter the key : ')
#     print(d[key])
#
# except KeyError:
#     print('error')
#
# except:
#     print('error')
#

# eg


# try:
#     n1=int(input('n1 ='))
#     n2=int(input('n2='))
#     n3=n1/n2
#
# except ZeroDivisionError as s:
#     print(s)
#     print(type(s))
#
# except ValueError as e:
#     print(e)
#     print(type(e))
#
# except Exception as e:
#     print(e)
#     print(type(e))

# eg

# class MyException(Exception):
#     pass
# try:
#     n=int(input('enter age : '))
#     if(n<18):
#         raise MyException('not eligible for voting')
#     else:
#         print('eligible for voting')
#
# except MyException as e:
#     print(e)

#ask the user to enter a number if the number is less than or equal to 0,
#raise a ValueError with the message 'Number must be Positive'

# try:
#     n=int(input('enter number : '))
#     if n<=0:
#         raise ValueError('Number must be positive')
#     else:
#         print('number is positive')
# except ValueError as e:
#     print(e)


#ask the user to enter the password if its length is less then 8 character raise
#a customException InvalidPassword with the message (Password should be a character)

# class InvalidPassword(Exception):
#     pass
# try:  
#     password=input('enter password : ')
#     if len(password)<8:
#         raise InvalidPassword('password should be 8 characters')
#     else:
#         print('password correct')
#
# except InvalidPassword as e:
#     print(e)

#Ask the user to enter an amount and if the amount<balance raise customException
# InsuffientBalanceError with the message('not enough balance.transaction failed')

# class InsuffientBalanceError(Exception):
#     pass
# try:
#     n=int(input('enter amount : '))
#     balance=60000
#     if (n>balance):
#         raise InsuffientBalanceError('not enough balance transaction falied')
#     else:
#         print(n)
#
# except InsuffientBalanceError as e:
#     print(e)
#
