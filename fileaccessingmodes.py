#a -append

# f=open('k.txt','a')
# f.write('python')
# f.close()

#1.write a program to append the contents from one file into another text file


# h=open('passedstudents.txt','r')
# f=open('k.txt','a')
# s=h.read()
# f.write(s)
# f.close()



# appendread

# f=open('k.txt','a+')
# print(f.tell())
# f.write('python') #append
# print(f.tell())
#
# f.seek(0)
# print(f.tell())
# s=f.read()     #read
# print(s)

#delete text file

import os
os.remove('k.txt')
print('file is deleted')