list=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
b=set()
for i in list:
    for key,value in i.items():
        b.add(value)
print(b)