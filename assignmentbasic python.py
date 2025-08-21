# 1.write a program to find reverse of a number in a list.
list1=[1,2,3,4,5,6,7]
list1.reverse()
print(list1)
# 2.write a program to find secondlargest number without using sorting techniques.

# 3.write a program to print list in an zig-zag.
l1=[1,2,3,4]
l2=[5,6,7,8]
emp=[]
for a,b in zip(l1,l2):
    emp.extend([a,b])
emp.extend(l1[len(l2):])
emp.extend(l2[len(l1):])
print(emp)
# 4.how we access the elements in a set.
fruits={"apple","orange","banana"}
my_list=list(fruits)
print(fruits)
# 5.how are values are sorted in a dictionary.
dict1={"name":"mounika","age":22,"city":"bangolore"}
print(dict1)
