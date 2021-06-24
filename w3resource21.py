dic = {'1':['a','b'], '2':['c','d']}
list1=dic.get('1')
list2=dic.get('2')
new=[]
i=0
while i<len(list1):
    j=0
    while j<len(list1):
        c=list1[i]+list2[j]
        print(c)
        #new.append(c)
        j+=1
    i+=1
#print(new)