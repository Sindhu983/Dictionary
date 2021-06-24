d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
dict={}
for i in d1:
    if i in d2:
        d2[i]+=d1[i]
dict={**d1,**d2}
print(dict)
