# dic = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# for i in dic.items():
#     print(i)


list=[1,1,1,2,3,3,4,5,5]
my_dict={}
for i in range(len(list)):
    my_dict[list[i]]=list.count(list[i])
print(my_dict)
