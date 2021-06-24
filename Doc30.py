dic={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
dict={}
for key,value in dic.items():
    c=key.split()
    i=0
    while i<len(c)-1:
        d=c[i]+c[i+1]
        i+=1
        dict[d]=value
print(dict)