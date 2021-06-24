list_num=[1,2,3,4,5]
list_str=['a','b','c','d','e','f']
user=int(input("enter the num :"))
i=0
dic={}
while i<len(list_str):
    list_num.append(user)
    dic[list_num[i]]=list_str[i]
    i+=1
print(dic)