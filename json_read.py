# READ

# import json
#
# f=open("data.json",'r')
#
# content=json.load(f)
#
# print(content)
# print(content[0]['name'],content[0]['age'])
# print(content[1]['name'],content[1]['age'])
# f.close()



#WRITE

import json
content=[
    {'Title':'Book1','author':'john','price':200},
    {'Title':'Book2','author':'sam','price':300},
]
f=open('book.json','w')
json.dump(content,f)
f.close()