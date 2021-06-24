dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# sorted_dict = {}
# sorted_keys = sorted(dic,key=dic.get) 
# for x in sorted_keys:
#     sorted_dict[x] = dic[x]
# print(sorted_dict)


sort_values = sorted(dic.values()) 
sorted_dict = {}
for i in sort_values:
    for j in dic.keys():
        if dic[j] == i:
            sorted_dict[j] = dic[j]
            break
print(sorted_dict)

