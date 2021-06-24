my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
list=[]
for key,val in my_dict.items():
    if val>50:
        list.append(key)
a=[]
i=-1
while i>=-len(list):
    a.append(list[i])
    i-=1
print(a)