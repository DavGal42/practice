# 1.Implement list with class

# class MyList:
#     def __init__(self, *args):
#         self.data = [el for el in args]
    
#     def clear(self):
#         self.data = []
    
#     def append(self, el):
#         self.data += [el]

#     def pop(self, index=-1):
#         el = self.data[index]

#         if index != -1:
#            self.data = self.data[:index] + self.data[index + 1:]
#         else:
#             self.data = self.data[:index]

#         return el

#     def remove(self, el):
#         self.data = [item for item in self.data if item != el]

#     def insert(self, index, el):
#         self.data = self.data[:index] + [el] + self.data[index:]

#     def double(self):
#         self.data = self.data * 2

#     def shift(self):
#         self.data = self.data[1:]

#     def indexOf(self, el):
#         for i in range(len(self.data)):
#             if el == self.data[i]:
#                 return i
#         return -1

#     def __repr__(self):
#         return repr(self.data)
    
# ml = MyList(1, 4.2, True, 'Hello', None)
# print(ml)





# W3Resource Tasks
# 1.Write a Python program to import a built-in array module and display the namespace of the said module.

# import array
# for name in array.__dict__:
#     print(name)



# 2.Write a Python program to create a class and display the namespace of that class.

# class Car:
#     def __init__(self, year, name, color):
#         self.year = year
#         self.name = name
#         self.color = color
#     def __str__(self):
#         return 'Class of Car'
# for el in Car.__dict__:
#     print(el)



# 3.Write a Python program to create an instance of a specified class and display the namespace of the said instance.

# class Car:
#     def __init__(self, year, name, color):
#         self.year = year
#         self.name = name
#         self.color = color
#     def __str__(self):
#         return 'Class of Car'

# tesla = Car(2020, 'Model 3', 'White')
# print(tesla.__dict__)