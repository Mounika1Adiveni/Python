# if number is a even or odd:
# num=int(input("Enter a number:"))
# if num%2==0:
#     print("given number is a even")
# else:
#     print("given number is a odd")
#
# # find leap year or not:
# year=int(input("Enter year:"))
# if year%4==0:
#     print("it is a leap year")
# else:
#     print("it is NOT a leap year")
# prime number or not:
# def is_prime(number):
#     if number>1:
#         for i in range(2, number):
#             if number % i == 0:
#                 return False
#         return True
#     return False
# n=int(input("enter the number:"))
# print(is_prime(n))

# name="mounika"
# for name in name:
#    print(name[::-1])
#
# print("hello world")
#
# l=[1,2,30]
# s='x'
# l.append(s)
# print(l)

# removing duplicates in list
# my_list = [1, 2, 2, 3, 4, 4, 5]
# no_duplicates = list(set(my_list))
# print(no_duplicates)
#
# my_list = [1, 2, 2, 3, 4, 4, 5]
# no_duplicates = list(dict.fromkeys(my_list))
# print(no_duplicates)

# list1=['a','b','c','a','b','c']
# duplicates=[]
# for item in list1:
#     if item not in duplicates:
#         duplicates.append(item)
# print(duplicates)

# split="mounika", "chinni", "nani", "ammu"
# l=set(split)
# print(l)

# split = "mounika:chinni:nani:ammu"
# # l=split.split(":")
# l=list(dict.fromkeys(split))
# print(l)

# removing name spaces:
# name="mounika chinni"
# replace=name.replace(" ","")
# print(replace)

# conditional statements
# 1.simple if:
# n=int(input("enter a number:"))
# if n>=18:
#     print("your eligible to vote")

# # 2.if else:
# n=int(input("enter a number:"))
# if n>=18:
#     print("your eligible to vote")
# else:
#     print("your not eligible to vote")

# 3.if elif else:
# n=int(input("enter a number:"))
# if n>=18:
#     print("your eligible to vote")
# elif n>=7:
#     print("your age is not considerable")
# else:
#     print("your not eligible to vote")

# 4.nested if:
# a=10
# b=20
# c=30
# if a>b:
#     if a>c:
#       print(a)
#     else:
#       print(b)
# else:
#     if a<c:
#         print(c)
#     else:
#         print(a)

# iterative statements:
# for loop, while loop, nested loop:
# 1.for loop(sequence,range)

# *forloop in range:
# for i in range(10):
#     print(i)
# for i in range(10):
#     print(i, end=" ")

# for loop in sequence:
# str="mounikasree"
# for i in str:
#     print(i,end=" ")

# while loop:
# n=int(input("enter a number:"))
# i=0
# while i<=10:
#     print(i,end=" ")
#     i+=1
# nested loop:
# for i in range(5):
#     for j in range(5):
#         print(i, end='')
#     print()
#
# for i in range(5):
#     for j in range(i+1):
#         print('*', end='')
#     print()

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print('*', end='')
#     print()

# for i in range(5):
#     for j in range(1,i+1):
#         print(" ", end='')
#     for k in range(5,0):
#         print("* ", end='')
#     print()
















