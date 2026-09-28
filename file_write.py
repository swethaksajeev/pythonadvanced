#write

f=open('k.txt','w') #if file exists it will erase the contents and return its reference to f
                    #else it will create a new empty file and return its reference to f

#f.write(string)
# s="""   #multilinestring
#
#
#"""
f.write('hello\n')
f.write('python\n')
#f.writelines(list)
f.writelines(['hello\n','python\n'])
f.close()

