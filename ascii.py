print(chr(65))
print(chr(123))
print(ord('B'))
name="mindx"
print(min(name))
print(max(name))

num='123456789'
print(sorted(num))
print(sorted(num,reverse=True))

lst = [1, 2, 3,8]
print(lst)
lst.append(4)
lst.extend([5,6])
lst.insert(2,'a')
lst.remove('a')

lst = [1, 2, 3,4]
item=lst.pop()
item1=lst.pop(2)
print(item1)
clr=lst.clear()
print(item,lst)
print(clr,lst)

lst = [1, 2, 3, 2]
idx = lst.index(3)
print(idx)

lst1 = [1, 2, 3,4]
item1=lst1.pop(2)
print(item1)
