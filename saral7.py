dic={
     "first":"1", 
     "second": "2", 
     "third": "1", 
     "four": "5", 
     "five":"5", 
     "six":"9",
     "seven":"7"
}
result={}
for key,value in dic.items():
     if value not in result.values():
          result[key]=value
print(result)
          






     


