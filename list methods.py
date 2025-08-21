# insertion operations
# append():
colors=["violet", "indego", "blue", "green"]
print(colors.append("red"))
print(colors)
# insert():
animals=["cat","dog","bat","mouse","pig","horse","donkey","goat"]
animals.insert(0,"elephant")
print(animals)
# extend():
fruits=["apple","banana","orange"]
vegetables=["tomato","onion","carrot"]
fruits.extend(vegetables)
print(fruits)
# Adding tuple to list:
list1=[1,2,3,4,5,6,7,8,9,10]
list2=(10,20,30,40,50)
list1.extend(list2)
print(list1)
# Adding set to list:
branch=["ece","cse","eee",]
branch2={"b.com","mechanical","civil"}
branch.extend(branch2)
print(branch)
# # Adding dictionary to list:
# branch={"ece":1,"cse":2,"eee":3}
# branch.extend(branch2)
# print(branch)

# delete operation:
# pop():
cars=["mahindra", "toyota","honda","bmw"]
cars.pop()
print(cars)
print(cars.pop(2))
# remove():
cars=["mahindra", "toyota","honda","bmw"]
cars.remove("mahindra")
print(cars)
# del:
cars=["mahindra", "toyota","honda","bmw"]
del cars[2]
print(cars)
# clear():
cars=["mahindra", "toyota","honda","bmw"]
cars.clear()
print(cars)

# Update operation:
list1=[1,2,3,4,5]
list1[2]=[6,7,8,9]
print(list1)
list1[3]=["python"]
print(list1)

# sort():
list1=[100,30,2,35,4,65]
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

# reverse():
colors=["red","green","blue","yellow","purple"]
colors.reverse()
print(colors)
# length():
colors=["red","green","blue","yellow","purple"]
print(len(colors))
# index():
colors=["red","green","blue","yellow","purple"]
print(colors.index("green"))
print(colors.index("red"))
# count():
flowers=["lilly", "rose", "jasmin", "lotus","lilly", "rose"]
print(flowers.count("rose"))
print(flowers.count("lilly"))
print(flowers.count("jasmin"))
# copy():
flowers=["lilly", "rose", "jasmin", "rose"]
print(flowers.copy())






