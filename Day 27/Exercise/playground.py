# def add(*args):
#     total = 0
#     for n in args:
#         total +=n
#     return total
#
# print(add(1, 4, 6, 7, 8, 9, 9345, 32, 23, 12, 1, 5))

# def calc(n, **kwargs):
#     # print(kwargs)
#     # for key, value in kwargs.items():
#     #     print(key)
#     #     print(value)
#
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calc(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan", model="Pathfinder")
print(f'{my_car.make} {my_car.model}')