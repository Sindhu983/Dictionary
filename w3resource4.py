dic={"one":1,"two":2,"three":3,"four":4,"five":5}
user=input("enter the input :")
for key in dic.values():
    if user in dic:
        print("yes key is present in dic")
        break
    else:
        print("No,key is not present in dic")
        break