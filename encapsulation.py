# Access modifires:
# public access modifire:
# class parent:
#     publicdata="mindless"
#     def method1(self):
#         print(self.publicdata)
# class child(parent):
#     def method2(self):
#         print(self.publicdata)
# obj1=parent()
# obj2=child()
# obj1.method1()
# print(obj1.publicdata)
# obj2.method2()
# print(obj2.publicdata)

# protect access modifire:
# class parent:
#     _protecteddata="mindless"
#     def method1(self):
#         print(self._protecteddata)
# class child(parent):
#     def method2(self):
#         print(self._protecteddata)
# obj1=parent()
# obj2=child()
# obj1.method1()
# print(obj1._protecteddata)
# obj2.method2()
# print(obj2._protecteddata)

# private access modifire:
# class parent:
#     __privatedata="mindless"
#     def method1(self):
#         print(self.__privatedata)
# # class child(parent):
# #     def method2(self):
# #         print(self.__privatedata)
# obj1=parent()
# # obj2=child()
# obj1.method1()
# print(obj1.__privatedata)
# # obj2.method2()
# # print(obj2.__privatedata)

# class Student:
#     def __init__(self,firstName,lastName):
#         self.firstName = firstName
#         self.lastName = lastName
#     def getfirstname(self):
#         return self.firstName
#     def getlastname(self):
#         return self.lastName
#     print(object.getfirstname())
#     print(object.getlastname())

# import multipledispatch
# class employee:
#     __salary=30000
#     def get_salary(self):
#         return self.__salary
#     def set_salary(self,salary):
#         self.__salary=salary
#     def change_salary(self,increment):
#         self.__salary+=increment

def func(units):
    total_bill=0
    if units<=100:
        total_bill=units*5
    elif units<=200:
        total_bill=units*10
    else:
        total_bill=(100*5)+(100*7)+((units-200)*10)
    return total_bill
print(func(100))
print(f"Total bill is {func(100)}")




