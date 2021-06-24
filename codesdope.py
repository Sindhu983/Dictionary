name=[]
marks=[]
for i in range(3):
    student=input("enter the names :")
    mark=int(input("enter the marks :"))
    name.append(student)
    marks.append(mark)


for index in range(0,len(marks)):
    for j in range(0,len(marks)):
        if marks[index]>marks[j]:
            name[index],name[j]=name[j],name[index]
            marks[index],marks[j]=marks[j],marks[index]

dict={}
for k in range(0,len(marks)):
    dict[name[k]]=marks[k]
print(dict)
        
