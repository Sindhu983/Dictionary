num_list = [1, 2, 3, 4]
new_dict = current = {}
for x in num_list:
    current[x] = {}
    current = current[x]
print(new_dict)
