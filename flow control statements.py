# sequence or normal statements:
# a=20
# b=10
# c=a-b
# print(c)
# # conditional statements:
# # simple if:
# a=10
# b=15
# if a>b:
#     print("a is greater than b")
#
# biriyani_price=180
# budget=200
# if biriyani_price<budget:
#     print("alexa,add biriyani to cart")
# # if-else statement
# apple=170
# budget=180
# if (apple<=budget):
#     print("alexa,add apple to cart")
# else:
#     print("alexa, do not add apple to cart")
# # if-elif-else:
# num=10
# if(num<=10):
#     print("num is less than 10")
# elif(num==100):
#     print("num is equal to 100")
# else:
#     print("num is greater than 100")

# vote=18
# if(vote<18):
#     print("your eligible to vote")
# else:
#     print("your not eligible to vote")
#
# # nested if:
# count=5
# if(count<5):
#     print("return count is less than 5")
# elif(count<5):
#     print("return count is equal to 5")
# else:
#     print("return count is greater than 5")

# looping statements:
# for loop:
# name="mounika"
# for i in name:
#   print(i)
#
# name="mounika"
# for i in name:
#   print(i,end=",")
#
# # while loop:
# i=1
# while(i<5):
#     print(i)
#     i=i+1
#
# count=5
# while(count>0):
#     print(count)
#     count=count-1
#
# count=5
# while(count>=10):
#     print(count)
#     count=count-1
# else:
#     print("return count is greater than 0")
# # nested loop:
# i=1
# while(i<=3):
#     for k in range(1,4):
#         print(i,'*',k,'=',(i*k))
#     i=i+1
#     print(i)
#
# # control statements:
# # pass statement:
# i=1
# while(i<=3):
#     pass
# for i in range(1,4):
#     pass
# if(i==2):
#     pass

# continue ststement:
# for i in range(1,4):
#     if(i%2==0):
#         continue
#         print(i)
# # break statement:
# i=1
# while(i<=10):
#     if(i==5):
#         break
#         print(i)



# def print_square(n):
#     for i in range(n):
#         print('*' * n)
# print_square(5)
#
# def print_triangle(n):
#     for i in range(1,n+1):
#         print('*' * i)
# print_triangle(5)
#
#
# def reverse_triangle(n):
#     for i in range(n,0,-1):
#         print('*' * i)
# reverse_triangle(5)
#
# def pyramid(n):
#     for i in range(n):
#         print(' ' * (n - i - 1), end='')
#         print('*' * (2 * i + 1))
# pyramid(5)
#
# def greet(name, message="Hello"):
#     print(f"{message}, {name}!")
#
# greet("Alice")
# greet("Bob", "Hi")
# def greet(name,message):
#     print(f"{message}, {name}!")
#     greet("Alice", "Hello")
#     greet("Bob", "Hi")

# for i in range(5,0,-1):
#     for j in range(5,0,-1):
#         print(j,end=' ')
#     print()

# for i in range(69,64,-1):
#     for j in range(1,6):
#         print(chr(i),end=' ')
#     print()

# for i in range(1,6):
#     for j in range(69,64,-1):
#         print(chr(i),end=' ')
#     print()

# for i in range(1,6):
#     for j in range(69,64,-1):
#         print(chr(j),end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# for i in range(65,70):
#     for j in range(65,i+1):
#         print(chr(i),end=' ')
#     print()

# for i in range(1,6):
#     for j in range(6,i,-1):
#         print("*",end=' ')
#     print()
#
# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end=' ')
#     print()

# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(i,end=' ')
#     print()

# for i in range(1,6):
#     for j in range(5,0,-1):
#         print(j,end=' ')
#     print()
# for i in range(1,6):
#     for j in range(i,i-1,1):
#         print(i,end=' ')
#     print()

# rows=5
# for i in range(rows,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# rows=5
# for i in range(65,70):
#     for j in range(65,i-1,1):
#         print(chr(i),end=" ")
#     print()

# for x in range(1,6):
#     for y in range(5,x,-1):
#         print(" ",end=" ")
#     for z in range(0,x):
#         print(" *",end=" ")
#     print()

# for x in range(1,6):
#     for y in range(5,x,-1):
#         print(" ",end=" ")
#     for z in range(0,x):
#         print(x,end=" ")
#     print()

# for x in range(1,6):
#     for y in range(5,x,-1):
#         print(" ",end=" ")
#     for z in range(1,x+1):
#         print(z,end=" ")
#     print()

# for x in range(1,6):
#     for y in range(5,x,-1):
#         print(" ",end=" ")
#     for z in range(0,x):
#         print(chr(x+64),end=" ")
#     print()

# for x in range(1,6):
#     for y in range(5,x,1):
#         print(" ",end=" ")
#     for z in range(1,x-1):
#         print(chr(65),end=" ")
#     print()
# inc=1
# for x in range(5,0,-1):
#     for y in range(x,0,-1):
#         print(" ", end="")
#     print("*"*inc)
#     inc+=2;

# num=1
# inc=1
# for x in range(5,0,-1):
#     for y in range(x,0,-1):
#         print(" ", end="")
#     print(str(num)*inc)
#     num+=1
#     inc+=2

# inc=1
# for x in range(65,70):
#     for y in range(65,x+1):
#         print(" ", end="")
#     print(chr(65)*inc)
#     inc+=2;





















