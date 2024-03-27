# import random
# import time

# class Unit:

#     def __init__(self, name, health=100):
#         self.name = name
#         self.health = health

#     def kill(self, other_unit):
#         while True:
#             choice = random.choice((self, other_unit))
#             if choice == self:
#                 print(f'{self.name} Kill {other_unit.name}\nHealt -> {self.health}, {other_unit.health}')
#                 other_unit.health -= 20
#             else:
#                 print(f'{other_unit.name} Kill {self.name}\nHealt -> {self.health}, {other_unit.health}')
#                 self.health -= 20
#             if self.health == 0:
#                 print(f'Win {other_unit.name}')
#                 break
#             elif other_unit.health == 0:
#                 print(f'Win {self.name}')
#                 break
#             time.sleep(1)


# unit1 = Unit('Shirak')
# unit2 = Unit('Anzhela')
# unit1.kill(unit2)
# print(unit1.health)
# print(unit2.health)


# --------------> task 1



# import math

# class Circle:
#     def __init__(self, x=0, y=0, r=1):
#         self.x = x
#         self.y = y
#         self.r = r

#     def area(self):
#         return math.pi * self.r ** 2

#     def perimeter(self):
#         return 2 * math.pi * self.r

#     def scale(self, k):
#         self.r *= k

#     def is_intersect(self, other):
#         distance_between_centers = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
#         sum_of_radii = self.r + other.r
#         return distance_between_centers <= sum_of_radii

# circle1 = Circle(0, 0, 1)
# circle2 = Circle(2, 0, 1)

# print("Area of circle 1:", circle1.area())
# print("Perimeter of circle 1:", circle1.perimeter())

# print("Area of circle 2:", circle2.area())
# print("Perimeter of circle 2:", circle2.perimeter())

# print("Do circle 1 and circle 2 intersect?", circle1.is_intersect(circle2))

# circle1.scale(2)
# print("Area of circle 1 after scaling by 2:", circle1.area())
# print("Perimeter of circle 1 after scaling by 2:", circle1.perimeter())


# --------------> task 2



# class Parent:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.children = []

#     def info(self):
#         print(f"Name: {self.name}, Age: {self.age}")

#     def comfort_child(self, child):
#         print(f"{self.name} comforts {child.name}.")
#         child.set_calm()

#     def feed_child(self, child):
#         print(f"{self.name} feeds {child.name}.")
#         child.set_not_hungry()


# class Child:
#     def __init__(self, name, age, calm=False, hungry=True):
#         self.name = name
#         self.age = age
#         self.calm = calm
#         self.hungry = hungry

#     def set_calm(self):
#         self.calm = True

#     def set_not_calm(self):
#         self.calm = False

#     def set_hungry(self):
#         self.hungry = True

#     def set_not_hungry(self):
#         self.hungry = False

#     def info(self):
#         print(f"Name: {self.name}, Age: {self.age}, Calm: {self.calm}, Hungry: {self.hungry}")




# parent = Parent("John", 40)
# child = Child("Alice", 10)

# parent.info()  
# child.info()   

# parent.comfort_child(child)  
# parent.feed_child(child)     

# child.info()   


# --------------> task 3