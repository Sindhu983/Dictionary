my_dict = {'x':500, 'y':5874, 'z': 560, 'r':600}
max=0
min=0
# for key in my_dict.keys():
#     if my_dict[key]>max:
#         max=my_dict[key]
#     if my_dict[key]<max:
#         min=my_dict[key]
# print("maximum",max)
# print("second max",min)

for key in my_dict.keys():
    if my_dict[key]>max:
        max=my_dict[key]
        #max=min
    elif my_dict[key]<max<min:
        min=my_dict[key]
print(min)
print(max)



