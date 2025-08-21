"""1.prints the sum of current numbers and previous numbers.
write a python program to iterate the first 10 numbers  and each iteration prints the current and previous numbers."""
# previous=None
# for current in range(10):
#     if previous is None:
#         print(current)
#     else:
#         sum=previous+current
#         print(previous,current, sum)
#         previous=current
#     previous=current
# # sum=0
# for i in range(1,11):
#     print("previous values sum",sum)
#     sum=sum+i
#     print("current values",sum)
# print("Sum of all values",sum)
# 2.write a python program to such a given number from a list.
# list=[1,2,3,4,5,6,7,8,9]
# if 5 in list:
#     print("The number is in the list")
# else:
#     print("The number is not in the list")
# 3.write a python program to print whether the given number is prime number or not.
# num=10
# if num>3:
#     print("the given number is a prime number")
# else:
#     print("the given number is NOT a prime number")
# 4.write a program that take the user input of 3 angles and will found out whether it is a triangle or not.
# angle1=int(input("enter angle in degrees:"))
# angle2=int(input("enter angle in degrees:"))
# angle3=int(input("enter angle in degrees:"))
# if angle1>0 and angle2>0 and angle3>0:
#     if angle1+angle2+angle3==180:
#         print("it is a triangle")
#     else:
#         print("it is a quadratic")
# else:
#     print("it is not a triangle")
# 5.write a program that take user input selling price and cost price and whether it is a loss or profit.
# cost_price=int(input("enter cost_price:"))
# if cost_price>1000:
#     print("it is a profit")
# else:
#     print("it is a loss")
# 6.print the following patterns.
# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(i,end=" ")
#     print()
# 7.print the pyramid patterns.
# rows=int(input("Enter the row size of the pattern: "))
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(" ",end="")
#     for k in range(1,2*i):
#         print("*",end="")
#     print()
"""8.calculate the sum of all the numbers from 1 to given number, write a
program to accepts the number from a user and calculate the sum of all numbers 1 to given number."""
# n=int(input("Enter a number: "))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print("The sum of ",i," is ",sum)

# 9.write a program to display all prime numbers with in a range.
# for i in range(1,20):
#     if i % 2 == 0:
#         print("print all prime numbers between 1 and 20")
#     elif i % 2 != 0:
#         print("not prime numbers between 1 and 20")
#     else:
#         print("prime numbers between 1 and 20")
# 10.Reverse a given integer number.
# num=int(input("Enter a number: "))
# integer=1,2,3,4,5
# sum=reversed(integer)
# print(sum)
# 11.reverse pyramid pattern.
# rows=int(input("Enter the number of rows: "))
# for i in range(rows,0,-1):
#     for j in range(rows-i):
#         print(" ",end="")
#     for k in range(1,2*i):
#         print("*",end=" ")
#     print()



