
dict =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']
}
count=0

# ctr = sum(map(len, dict.values()))
# print("Total values :",ctr)
for i in dict.values():
    for j in i:
        count+=1
print("Total values",count)




