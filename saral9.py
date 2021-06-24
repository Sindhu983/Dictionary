
# def count_letter(word):
#     count={}
#     for x in word:
#         count[x]=word.count(x)
#     return count
# print(count_letter('mississippi'))

str='mississippi'
list1=[]
list2=[]
count=0
i=0
while i<len(str):
    if str[i] not in list1:
        list1.append(str[i])
    if str[i]=='m':
        count+=1
    elif str[i]=='i':
        count+=1
    elif str[i]=='s':
        count+=1
    elif str[i]=='p':
        count+=1
    else:
        pass
    i+=1
    print(count)
print(list1)







