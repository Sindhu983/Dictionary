num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
dic={}
for key,value in num.items():
    dic[key]=sorted(value)
print(dic)