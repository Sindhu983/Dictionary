# students = {'Aex':{'class':'V',
#         'rolld_id':2},
#         'Puja':{'class':'V',
#         'roll_id':3}}
# for a in students:
#     print(a)
#     for b in students[a]:
#         print (b,':',students[a][b])
		

list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
b=set()
result={}
for i in list:
    for key,value in i.items():
        result[key]+=value
print(result)
        