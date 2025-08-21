# list1=[1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e','f']
# print(list1)
# print(list1[0:])
# print(list1[:])
# print(list1[0:10])
# print(list1[:10])
# print(list1[10:16])
# print(list1[10:])

def func(units):
    total_bill=0
    if units<=100:
        total_bill=units*5
    elif units<=200:
        total_bill=units*10
    else:
        total_bill=(100*5)+(100*7)+((units-200)*10)
    return total_bill
print(func(100))
print(f"Total bill is {func(100)}")





