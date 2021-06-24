# a=['S001', 'S002', 'S003', 'S004']
# b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# c=[85, 98, 89, 92]
# dic={}
# list=[]
# i=0
# while i<len(a):
#     dic1={}
#     dic1[b[i]]=c[i]
#     dic[a[i]]=dic1
#     i+=1
# list.append(dic)
# print(list)


a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]
list=[]
for key in range(len(a)):
    d={a[key]:{b[key]:c[key]}}
    list.append(d)
print(list)


