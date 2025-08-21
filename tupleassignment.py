# 1. Write a Python program to create a tuple.
tuple1=(1,2,3,4,5,6,7)
# 2. Write a Python program to create a tuple with different data types.
datatypes=('a',1,20.8,True,3+4j)
# 3. Write a Python program to create a tuple with numbers and print one item.
# tuple1=(1,2,3,4,5,6,7)
# print(tuple1[3])
# 4. Write a Python program to unpack a tuple in several variables.
# info=("mindx",15,"bangolore")
# (name,age,location)=info
# print(name)
# print(age)
# print(location)
# 5. Write a Python program to add an item in a tuple.
# list1=("apple","banana","cherry")
# list2=list(list1)
# print(list2)
# list2.append("mango")
# print(list2)
# 6. Write a Python program to convert a tuple to a string.
# tuple1=("cow","dog","cow","cat")
# string=str(tuple1)
# print(string)
# 7. Write a Python program to get the 4th element and 4th element from last of a tuple.
# tuple1=("apple","banana","cherry","mango","orange","grapes","papaya")
# print(tuple1[-4:-3])
# 8. Write a Python program to create the colon of a tuple.
# colon=(1,2,3,4,5,6,7)
# print("colons",colon)
# colon1=colon[:]
# print("colon1:",colon1)
# print("colonid:",id(colon))
# print("colon1id:",id(colon1))
# 9. Write a Python program to find the repeated items of a tuple.
# fruits={'apple','banana','mango'}
# print(tuple(fruits))
# fruits1=('apple','grapes','banana','cherry')
# fruits2=fruits.intersection(fruits1)
# print(fruits2)
# tuple1=(1,2,2,3,4,2)
# new_tuple=set(tuple1)
# for i in  tuple1:
#     if tuple1.count(i)>1:
#         print(i)
# 10. Write a Python program to check whether an element exists within a tuple.
# n=int(input("enter a number:"))
# tuple2=(1,2,3,4,5,6,7)
# if n in tuple2:
#     print("exists")
# 11. Write a Python program to convert a list to a tuple.
# list1=[1,2,3,4,5,6,7]
# print(tuple(list1))
# 12. Write a Python program to remove an item from a tuple.
# fruits=['apple','banana','mango']
# print(tuple(fruits))
# fruits.remove('banana')
# print(fruits)
# 13. Write a Python program to slice a tuple.
# fruits=('apple','banana','mango')
# print(fruits[:])
# print(fruits[::-1])
# print(fruits[::])
# 14. Write a Python program to find the index of an item of a tuple.
# fruits=('apple','banana','mango','grapes','orange')
# print(fruits.index('banana'))
# print(fruits.index('orange'))
# 15. Write a Python program to find the length of a tuple.
# fruits=('apple','banana','mango','grapes','orange')
# print(len(fruits))
# 16. Write a Python program to convert a tuple to a dictionary.
# tuple_data = (('a', 1), ('b', 2), ('c', 3))
# dictionary = dict(tuple_data)
# print(dictionary)
# 17. Write a Python program to unzip a list of tuples into individual lists.
# list_data = [('a', 'mounika'), ('b', 'ammu'), ('c', 'chinni')]
# names,grades=zip(*list_data)
# names=list(names)
# grades=list(grades)
# print(names)
# print(grades)
# 18. Write a Python program to reverse a tuple.
# fruits=('apple','banana','mango','grapes','orange')
# rev=fruits[::-1]
# print(rev)
# 19. Write a Python program to convert a list of tuples into a dictionary.
# names=[('apple',100),('banana',40),('mango',150),('grapes',60),('orange',100)]
# print(dict(names))
# 20. Write a Python program to print a tuple with string formatting.
# tuple1=("mounika",20)
# print(f"my name is:" ,tuple1[0])
# print(f"my age is:" ,tuple1[1])
# 21. Create a tuple with single item 23.
# item=(23,)
# print(item)
# 22. Unpack the tuple into 5 variables.
# unpack=("apple","banana","mango","grapes","orange")
# a,b,c,d,e=unpack
# print("var a:",a)
# print("var b:",b)
# print("var c:",c)
# print("var d:",d)
# print("var e:",e)
# 23. Swap two tuples in Python.
# tuple=('apple','banana','mango','grapes','orange')
# tuple1=(1,2,3,4,5,6,7)
# print("Tuple1:",tuple)
# print("Tuple:",tuple1)
# 24. Copy specific elements from one tuple to a new tuple.
# tuple2=(1,2,3,4,5,6,7)
# new_tuple=(tuple2[0],tuple2[1],tuple2[2],tuple2[3],tuple2[4])
# print(new_tuple)
# 25. Modify the tuple.
# tuple2=(1,2,3,4,5,6,7)
# mod_tuple=list(tuple2)
# mod_tuple[1]=20
# mod_tuple[3]=30
# print(mod_tuple)
# 26. Sort a tuple of tuples by 2nd item.
# tuple2=((4,2),(2,3))
# print(tuple2.sort[1])
# 27. Counts the number of occurrences of item 30 from a tuple.
# 28. Write a Python program to compute element-wise sum of given tuples.
# num=(1,2,3,4,5,6,7)
# num1=(10,20,40,50)
# sum=num+num1
# print(sum)
# 29. Write a Python program to sort a tuple by its float element.
# num=((3.5),(4.5),(2.5))
# num2=tuple(sorted(num))
# print(num2)
# 30. Write a Python program to replace last value of tuples in a list.
# tuple1=[(1,2),(2,4),(3,4)]
# update=[]
# for i in tuple1:
#     new_tuple=i[:-1]+(100,)

#     update.append(new_tuple)
# print(update)
# 31. Write a Python program to Extract tuples having K digit elements.
# tuple_list = [(12, 34, 56), (123, 456, 789), (1, 23, 45), (10, 20, 30)]
# k=2
# for i in tuple_list:
#     if k==len(tuple_list):
#       print(k)
# 32. Write a Python program to Extract Symmetric Tuples.
# num=[(1,2,3),(2,2,3),(7,3,3)]
# result=[]
# for i in num:
#     if i==i[::-1]:
#         result.append(i)
# print(result)
# 33. Write a Python program to Sort Tuples by their Maximum element.
# tuple_list = [(1, 5, 3), (2, 1, 4), (6, 2, 8), (3, 7, 2)]
# sort_list=[]
# for i in tuple_list:
#     max=i[0]
#     for j in i:
#         if j>max:
#             max=j
#             sort_list.append((j,i))
# sort_list.sort()
# list=[i for _,i in sort_list]
# print(sort_list)
# 34. Write a Python program to Remove nested records from tuple.
# input_tuple = (1, (2, 3), 4, (5, 6, 7), 8, 'a', (9,))
# result=[]
# for item in input_tuple:
#     if not isinstance(item, tuple):
#         result.append(item)
# nested=tuple(result)
# print(input_tuple)
# print(nested)
# 35. Write a Python program to Elements Frequency in Mixed Nested Tuple.
# input_tuple = (1, (2, 3, 2), 4, (3, 5, 1), 'a', (2, 'a'))
# freq={}
# for item in input_tuple:
#     if isinstance(item, tuple):
#         for nested_item in item:
#             if nested_item in freq:
#                 freq[nested_item] += 1
#             else:
#                 freq[nested_item] = 1
#     else:
#         if item in freq:
#             freq[item] += 1
#         else:
#             freq[item] = 1
# print(freq)
# print(tuple1)






































