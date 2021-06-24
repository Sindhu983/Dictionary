my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
list=[]
for key in my_dict.values():
    if key>50:
        list.append(key)
print(list)