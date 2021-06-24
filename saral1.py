dict1={1:10, 2:20}
dict2={3:30,2:40}
dict3={5:50,6:60}
dict={}
for i in dict1:
    if i in dict2:
        dict2[i]+=dict1[i]
dict={**dict1,**dict2,**dict3}
print(dict)
 