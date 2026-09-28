
# 1.file read
# 2.file write
# 3.file append
# 4.file search
# 5.file delete
# 6exit

def file_read():
    filename = input('enter file name : ')
    f=open(filename, 'r')
    s=f.read()
    print(s)
    f.close()

def file_write():
    filename=input('enter filename: ')
    f1=open(filename,'w')
    g=input('enter content : ')
    f1.write(g)
    print('content successfully written')
    f1.close()

def file_append():
    filename = input('enter filename: ')
    f2 = open(filename, 'a')
    content=input('enter content : ')
    f2.write(content)
    print('successfully appended')
    f2.close()


def file_search():
    filename = input('enter filename: ')
    f=open(filename,'r')
    s=f.read()
    word=input('enter the word to search')
    if word in s:
        print('word',word,'is present')

    else:
        print('word', word, 'is not present')
    f.close()
def file_delete():
    import os
    d=input('enter file to be deleted : ')
    os.remove(d)
    print('file deleted')

while(True):
    print('Menu Driven-File Operation')
    print('1.File Read')
    print('2.File Write')
    print('3.File Append')
    print('4.File Search')
    print('5.File Delete')
    print('6.Exit')

    ch=int(input('enter the choice: '))
    if ch==1:
        file_read()
    elif ch==2:
        file_write()
    elif ch==3:
        file_append()
    elif ch==4:
        file_search()
    elif ch==5:
        file_delete()
    else:
        exit()