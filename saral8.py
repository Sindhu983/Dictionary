# dic1=[]
# dic2=[]
# dic={}
# num=int(input("enter the number :"))
# i=1
# while i<=num:
#     student=input("enter the name :")
#     marks=int(input("enter the number :"))
#     dic1.append(student)
#     dic2.append(marks)
#     i+=1
# j=0
# while j<len(dic1):
#     dic[dic1[j]]=dic2[j]
#     j+=1
# print(dic)

dict={}
for i in range(10):
    names=input("enter the name :")
    marks=int(input("enter the marks :"))
    dict[names]=marks
print(dict)
