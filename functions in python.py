def name(fname,mname,lname):
    print("HELLO",fname,mname,lname)
name("A","B","C")

# rows=5
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print(" ")
#
# for i in range(rows):
#     for j in range(i+1):
#         print(chr(65+j),end=" ")
#     print(" ")
#
# for i in range(rows):
#     for j in range(rows-i-1):
#         print(chr(65+j),end=" ")
#     print(" ")
#
# for i in range(rows):
#     for j in range(i+1):
#         print(chr(65+i),end=" ")
#     print(" ")
#
# for i in range(rows):
#     for j in range(1,rows-1):
#         for j in range(i-1):
#             print(i,end=" ")
#     print(" ")
#
# for i in range(5):
#     for j in range(i+1):
#       print("*",end=" ")
#     print(" ")

# n=5
# for i in range(n,0,-1):
#     print("*" * n)
#
# for i in range(n):
#     print("*" * (i+1))
#
#
# for i in range(n,0,-1):
#     print("*" * i)
#
# for i in range(n):
#     pyramid1=" " * (n -i -1)
#     stars=" "* (2 *i +1)
#     print(pyramid1 + stars)
#
# n = 5
# for i in range(n):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))
#
# for i in range(n - 1, -1, -1):
#     print(" " * (n - i - 1) + "*" * (2 * i + 1))
#
# for i in range(1,n+1):
#     print(str(i)*i)
#
# for i in range(n-2,-1,-1):
#     print(str(i)*i)

n=5
for i in range(1,n+1):
    for j in range(i):
        print((i+j)%2,end=" ")
    print(" ")

print("\n normal pyramid")
for i in range(5):
    x="*"
    x=x*i
    print(f'{x: ^10}')

print("\n invert pyramid")
for i in range(5):
    x="*"
    x=x*(5-i)
    print(f'{x: ^10}')

print("\n leftside pyramid")
for i in range(5):
    x="*"
    x=x*i
    print(f'{x: <10}')

print("\n rightside pyramid")
for i in range(5):
    x="*"
    x=x*i
    print(f'{x: >10}')


