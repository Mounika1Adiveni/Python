# from abc import ABC, abstractmethod
# import math
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class circle(shape):
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return math.pi * self.radius **2
# class rectangle(shape):
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
# circle = circle(10)
# print('circle.area:',circle.area())
# rectangle = rectangle(10,10)
# print('rectangle.area:',rectangle.area())

from abc import ABC, abstractmethod
class vehical(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class car(vehical):
    def start(self):
        print("car engine start")
    def stop(self):
        print("car engine stop")
class motorcycle(vehical):
    def start(self):
        print("motorcycle engine start")
    def stop(self):
        print("motorcycle engine stop")
my_car = car()
my_car.start()
my_car.stop()
my_motorcycle = motorcycle()
my_motorcycle.start()
my_motorcycle.stop()