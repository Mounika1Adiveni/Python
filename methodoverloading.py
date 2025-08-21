# same method different datatypes:


# from multipledispatch import dispatch
# class addition:
#     @dispatch(int,int)
#     def add(self,a,b):
#         return a+b
#     @dispatch(float,float,float)
#     def add(self,a,b,c):
#         return a+b+c
#     @dispatch(str,str,str)
#     def add(self,a,b,c):
#         return a+b+c

# obj = addition()
# print(obj.add(1.0,2.5,3.8))
# print(obj.add(1,2))
# print(obj.add("mindx","solutions","python"))

# from multipledispatch import dispatch
# class addition:
#     @dispatch(int,int)
#     def add(self,a,b):
#         return a+b
#     @dispatch(int,int,int)
#     def add(self,a,b,c):
#         return a+b+c
#     @dispatch(int,float)
#     def add(self,a,b,c):
#         return a+b+c
# object=addition()
# print(object.add(1,2))
# print(object.add(1,2,3))
# print(object.add(10,2025))

# from multipledispatch import dispatch
# class addition:
#     @dispatch(int,int)
#     def add(self,a,b):
#         return a+b
#     @dispatch(float,float,float)
#     def add(self,a,b,c):
#         return a+b+c
#     @dispatch(str,str,str)
#     def add(self,a,b,c):
#         return a+b+c
# obj = addition()
# print(obj.add(1,2))
# print(obj.add(1,2))
# print(obj.add("python","full","stack"))

# from multipledispatch import dispatch
# class addition:
#     @dispatch(int,int)
#     def add(self,a,b):
#         return a+b
#     @dispatch(int,int,float)
#     def add(self,a,b,c):
#         return a+b+c
#     @dispatch(str,str,str)
#     def add(self,a,b,c):
#         return a+b+c
# obj = addition()
# print(obj.add(1,2))
# print(obj.add(1,2,2.3))
# print(obj.add("python","full,"stack"))

# from multipledispatch import dispatch
# class addition:
#     @ dispatch(int,int)
#     def add(self,a,b):
#         return a+b
#     @ dispatch(int,int,int,int)
#     def add(self,a,b,c,d):
#         return a+b+c+d
#     @ dispatch(int,int,int,float)
#     def add(self,a,b,c,d):
#         return a+b+c+d
#     @dispatch(str,str,str)
#     def add(self,a,b,c):
#         return a+b+c
# obj = addition()
# print(obj.add(1,2))
# print(obj.add(1,2,3,6))
# print(obj.add(1,3,6,3.5))
# print(obj.add("python","full","stack"))

