# dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# count=0
# for i in dict.values():
#     for j in i:
#         count+=1
# print(count)


# dic1={1:{'key1': 1, 'key2': 3, 'key3': 2},2: {'key1': 1, 'key2': 2}}
# for i in dic1.items():
#     for j in dic1:
#         print("key1 is present in both 1 and 2")
#         break
#     else:
#         print("key3 is not not present in both")

# from random import sample
# l = ['python', 'coding', 'list', 'string', 'solution']
# for i in l:
#     print(''.join(sample(i, len(i)))



# dic={'#FF0000': 'Red', '#800000': 'Maroon', '#FFFF00': 'Yellow', '#808000': 'Olive'}
# c=0
# for value in dic:
#     a=len(dic[value])
#     c+=a
# print(a)


a=[["Bengali"],["Tamil"],["Tamil"],["Tamil"],["Hindi"],["Bengali"],["Telugu"],["Malayalam"],["Malayalam"],["Marathi"]]
list=[]
for ele in a:
    list.extend(ele)
#print(list)
i=0
dic={}
while i<len(list):
    j=0
    count=0
    while j<len(list):
        if list[i]==list[j]:
            count+=1
        j+=1
    dic[list[i]]=count
    i+=1
print(dic)

    
    
