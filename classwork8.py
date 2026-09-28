 # #write a program to read a text file and displays the number of lines in a file

# f=open('k.txt','r')
# s=f.readlines()
# print(s)
# l=len(s)
# print('length = ',l)
# f.close()

# # #write a program to display the number of words in a file
#
# f=open('k.txt','r')
# s=f.read()
# count=0
# for i in s.split():
#     count=count+1
# print(count)
# print(s)
# f.close()
#
# #or
# f=open('k.txt','r')
# s=f.read()
# print(s.split())
# print(len(s.split()))
# f.close()

# # #write a program to update the second line in a file

# f=open('k.txt','r')
# s=f.readlines()
# print(s)
# s[1]='java\n'
# f.close()
# f=open('k.txt','w')
# f.writelines(s)
# f.close()
# print(s)



# # #write a program to display the last 5 lines in a file

# f=open('k.txt','r')
# s=f.readlines()
# last_five=s[-5:]
# for i in last_five:
#     print(i,end=' ')
# f.close()

#or

# f=open('k.txt','r')
# s=f.readlines()
# print(s[-5:])
# f.close()

#
# #program to search a particular word in a file

# word=input('enter the word : ')
# f=open('k.txt','r')
# s=f.read()
#
# if word in s:
#     print(word,'is in given txt',end=' ')
# else:
#     print(word,'not in given txt')
# f.close()

# #find the number of letters,digits,and spaces in a file

f=open('k.txt','r')
s=f.read()
letters=0
digits=0
spaces=0
for i in s:
    if i.isalpha():
        letters=letters+1
    elif i.isdigit():
        digits=digits+1
    elif i.isspace():
        spaces=spaces+1
f.close()
print('letters =',letters)
print('digits =',digits)
print('spaces =',spaces)

#reverse the lines in a file

f=open('k.txt','r')
s=f.readlines()
s=s[::-1]
f.close()
f=open('k.txt','w')
f.writelines(s)
f.close()

# A file totalstudents.txt contains the names of all students in a class,
# and a file passedstudents.txt contains the names of students who passed.txt the exam.
# Write a Python program to:
# Read the names from both files.
# # Find the students who did not pass.
# # Write their names to a new file named failed_students.txt, one name per line.
# #

f=open('totalstudents.txt','w')
f.writelines(['amal\n','arun\n','anu\n','kiran\n','suresh\n'])
g=open('passedstudents.txt','w')
g.writelines(['arun\n','anu\n','kiran\n','suresh\n'])
f=open('totalstudents.txt','r')
g=open('passedstudents.txt','r')
s1=f.readlines()
s2=g.readlines()
h=open('failedstudents.txt','w')
for i in s1:
    if i not in s2:
        h.write(i)
f.close()
g.close()
h.close()
