# def func1():
#     print("hello world")
# func1()
# def func2():
#     print("hello again")
# func2()
# def func3():
#     print("hello guys")
# func3()
#
# def decor(fun):
#     def wrapper():
#         print("before the function")
#         fun()
#         print("after the function")
#     return wrapper
#
# @decor
# def display():
#     print("hello welcome to python")
# display()
# def decor1(f):
#     print("Decorator 1")
#     return f
# @decor1
# def function():
#     print("hello world")
# function()
def webpage(func):
    def inner(name,login):
        if login == 'False':
            print("enter admin name")
            return
        return func(name,login)
    return inner
def webpage2(func1):
    def inner(name,login):
        if name == 'True':
            print("mounika")
            return
        return func1(name,login)
    return inner
@webpage
def home(name,login):
    print("welcome to home page")
@webpage
def orders(name,login):
    print("welcome to orders page")
def about():
    print("welcome to about page")
home('user','False')
orders('user','True')
about()



