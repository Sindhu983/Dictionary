a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
b=set()
for i in a:
    for key,value in i.items():
        if value>400:
            print(value)
        else:
            print(key)
