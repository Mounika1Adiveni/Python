# 1.right angled triangle:
# rows=int(input("Enter the number of rows: "))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# 2.inverted right triangle:
# rows=int(input("Enter the number of rows: "))
# for i in range(rows,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
# 3.pyramid pattern:
rows=int(input("Enter the number of rows: "))
for i in range(1,rows+1):
    for j in range(rows -i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end=" ")
    print()
# 4.inverted pyramid:
rows=int(input("Enter the number of rows: "))
for i in range(rows,0,-1):
    for j in range(rows -i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end=" ")
    print()
# 5.diamond pattern:
# rows=int(input("Enter the number of rows: "))
# for i in range(1,rows+1):
#     for j in range(rows -i):
#         print(" ",end="")
#     for k in range(1,2*i):
#         print("*",end="")
#     print()
# for i in range(rows-1,0,-1):
#     for j in range(rows-i):
#         print(" ",end="")
#     for k in range(1,2*i):
#         print("*",end="")
#     print()
# 6.hollow square:
# rows=int(input("Enter the number of rows: "))
# for i in range(1,rows+1):
#     for j in range(1,rows+1):
#         if i==1 or i==rows or j==1 or j==rows:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# 7.hollow right-angle triangle:
# rows=int(input('enter the number of rows: '))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         if j==1 or i==rows or i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# 8.hollow inverted right triangle:
# rows=int(input("Enter the number of rows: "))
# for i in range(rows,0,-1):
#     for j in range(1,i+1):
#         if j==1 or i==rows or i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# 9.hollow pyramid pattern:
# rows=int(input("Enter the number of rows: "))
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         if k==1 or k==2*i-1 or i==rows:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# # 10.hollow inverted pyramid:
# rows=int(input("Enter the number of rows: "))
# for i in range(rows,0,-1):
#     for j in range(rows-i):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         if k==1 or k==2*i-1 or i==rows:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# 11.holloe diamond pyramid:
# rows=int(input("Enter the number of rows: "))
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         if k==1 or k==2*i-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# for i in range(rows-1,0,-1):
#     for j in range(rows-i):
#         print(" ",end=" ")
#     for k in range(1,2*i):
#         if k==1 or k==2*i-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# 12.number right angle:
# rows=int(input("Enter the number of rows: "))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# 13.inverted number:
# rows=int(input("Enter the number of rows: "))
# for i in range(rows,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# 14.number pyramid:
# rows=int(input("Enter the number of rows: "))
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     for l in range(i-1,0,-1):
#         print(l,end=" ")
#     print()
# 15.number inverted pyramid:
# rows=int(input("Enter the number of rows: "))
# for i in range(rows,0,-1):
#     for j in range(rows-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     for l in range(i-1,0,-1):
#         print(l,end=" ")
#     print()
# 16.number diamond pattern:
# rows=int(input("Enter the number of rows: "))
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     for l in range(i-1,0,-1):
#         print(l,end=" ")
#     print()
# for i in range(rows-1,0,-1):
#     for j in range(rows-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     for l in range(i-1,0,-1):
#         print(l,end=" ")
#     print()
# 17.alphabet traingle:
# rows=int(input("Enter the number of rows: "))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(chr(64+j),end=" ")
#     print()
# 18.alphabet inverted:
# rows=int(input("Enter the number of rows: "))
# for i in range(rows,0,-1):
#     for j in range(1,i+1):
#         print(chr(64+j),end=" ")
#     print()
# 19.alphabet pyramid:
# rows=int(input("Enter the number of rows: "))
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(chr(64+k),end=" ")
#     for l in range(i-1,0,-1):
#         print(chr(64+l),end=" ")
#     print()
# 20.alphabet inverted pyramid:
# rows=int(input("Enter the number of rows: "))
# for i in range(rows,0,-1):
#     for j in range(rows-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(chr(64+k),end=" ")
#     for l in range(i-1,0,-1):
#         print(chr(64+l),end=" ")
#     print()
# 21.alphabet diamond:
# rows=int(input("Enter the number of rows: "))
# for i in range(1,rows+1):
#     for j in range(rows-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(chr(64+k),end=" ")
#     for l in range(i-1,0,-1):
#         print(chr(64+l),end=" ")
#     print()
# for i in range(rows-1,0,-1):
#     for j in range(rows-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(chr(64+k),end=" ")
#     for l in range(i-1,0,-1):
#         print(chr(64+l),end=" ")
#     print()
# 22.continue numbers triangle:
# rows=int(input("Enter the number of rows: "))
# num=1
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num=num+1
#     print()
# 23.continue inverted triangle:
# rows=int(input("Enter the number of rows: "))
# num=1
# for i in range(rows,0,-1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num=num+1
#     print()
# 24.pascals triangle:
# rows=int(input("Enter the number of rows: "))
# for i in range(rows):
#     num=1
#     for j in range(rows-i):
#         print(" ",end=" ")
#     for k in range(i+1):
#         print(num,end=" ")
#         num=num*(i-k)
#     print()
# 25.hollow butterfly pattern:
# rows=int(input("Enter the number of rows: "))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         if j==1 or j==i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     for j in range(2*(rows-i)):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         if j==1 or j==i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# for i in range(rows,0,-1):
#     for j in range(1,i+1):
#         if j==1 or j==i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     for j in range(2*(rows-i)):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         if j==1 or j==i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#
# rows=int(input("Enter the number of rows: "))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()


# rows=int(input("Enter the number of rows: "))
# for i in range(rows,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()






