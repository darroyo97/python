# 3 main problems with structured programming

# 1. emphasis on functionality not data
# 2. Limitations
# 3. Gap in developer client comunication

# Object oriented Programming

# -Objects, classes, abstraction, encapsulation, inheritance, polymorphism

# objects - way to represent real life
# attributes = properties
# behavior - functionality

# class- container that defines your object
# example
# class Student:
#   properties(attributes):
# ....
#   functions(behavior)

# Abstactions - limit your attributes and functions to only items that pertain to the program
# encapsulation - limit access to data. only functions and classes that need access can have access.
# controlling access to data
# can only access data through public functions(interface)
# class Student:

# properties(attributes):
# .
# . private properties
# .
# functions(behavior)
# .
# . public functions
# . private functions

# Inheritance
# Child class inherits all of the properties and functions of parent class
# -Reusibility
# -Child class can extend on properties and functions
# -Reusabilty + Extensibility
# Parent

# Object (parent)
# .
# .
# .
# Object(child)

# ================================================================================
# ================================================================================
# ================================================================================
# outside a class is called a function, inside a class its called a method

# class Greeting:
#     def say_hello(self):
#         print("Hello there!")

# newGreetingObj = Greeting()

# newGreetingObj.say_hello()

# class example
# create a class students, that says good morning to each student

# class Student:
#     def greeting(self):
#         print("Good morning")

# daniela = Student()
# daniela.greeting()

# alex = Student()
# alex.greeting()

# juan = Student()
# juan.greeting()

# working with constructors
# A constructor is a special kind of method that Python calls
# when it instantiates an object by using definitions found in your class

# initializing (assigning value to) any instance variables that the object will need when it starts
# perform start-up tasks

# class Student:
#     def __init__(self):
#         print("consturctor is called")

#     def greeting(self):
#         print("good morning")

# Student()

# class Animal:
#     def __init__(self, name):
#         self.name = name

# dog = Animal("dog")
# cat = Animal("cat")
# horse = Animal("horse")

# print(dog.name)
# print(cat.name)
# print(horse.name)

# class Student:
#     # def __init__(self, name):
#     def __init__(self, name, lname):
#         self.name = name
#         # ^ called an instance variable
#         self.lname = lname
#         print(f'Hello there {self.name} {self.lname}')

# daniela = Student("daniela", "arroyo")
# print(student1.name)
# print(student1.lname)

# alina = Student("alina")
# joe = Student("joe")
# print(alina.name)
# print(joe.name)

# ====================================================================
# ====================================================================
# ====================================================================

# import datetime


# class Person:
#     def __init__(self, fname, lname, birthdate, address, email):
#         self.fname = fname
#         self.lname = lname
#         self.birthdate = birthdate
#         self.address = address
#         self.email = email

#     def age(self):
#         today = datetime.date.today()
#         age = today.year - self.birthdate.year
#         if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
#             age -= 1


# sammy = Person("Sammy", "Kry", datetime.date(1998, 8, 21), "123 Sesame Street", "sammy123@gmail.com")

# print(sammy.birthdate)

# ====================================================================
# ====================================================================
# ====================================================================

# class Person():
#     def __init__(self, name):
#         self.name = name
#         self.count = 0

#     def greeting(self):
#         print(f'hello {self.name} !')
#         self.count += 1

#     def printCount(self):
#         print(self.count)


# alina = Person("alina")

# alina.greeting
# alina.printCount()
# alina.greeting
# alina.printCount()


# ====================================================================
# ====================================================================
# # ====================================================================
# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.count = 0

#     def greet(self):
#         self._greet()

#     def _greet(self):
#         self.count += 1
#         if self.count > 1:
#             print("Stop being so nice")
#             self.__reset_count()
#         else:
#             print("Hello", self.name)

#     def __reset_count(self):
#         self.count = 0


# alex = Person("alex")

# alex.greet()

# ====================================================================
# ====================================================================
# ====================================================================

# class VString(str):
#     def reverse(self, name):
#         rstring = ""
#         for char in name:
#             rstring = char + rstring
#         return rstring


# my_string = VString("hello")
# print(my_string)
# print(my_string.capitalize())
# reverse_string = my_string.reverse("hello")
# print(reverse_string)

# Inheritance
# 3 ways that the parent and child classes can interact:
# Actions on the child imply an action on the parent.
# class Parent(object):
#     def implicit(self):
#         print("PARENT implicit()")


# class Child(Parent):
#     pass


# dad = Parent()
# son = Child()
# dad.implicit()
# son.implicit()

# Actions on the child override the action on the parent.
# class Parent(object):
#     def override(self):
#         print("PARENT override()")


# class Child(Parent):
#     def override(self):
#         print("CHILD override()")


# dad = Parent()
# son = Child()
# dad.override()
# son.override()

# Actions on the child alter the action on the parent.


# class Parent(object):
#     def altered(self):
#         print("PARENT altered()")


# class Child(Parent):
#     def altered(self):
#         print("CHILD, BEFORE PARENT altered()")
#         super(Child, self).altered()
#         print("CHILD, AFTER PARENT altered()")


# dad = Parent()
# son = Child()
# dad.altered()
# son.altered()


# ====================================================================
# ====================================================================
# ====================================================================


class Character:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health


class Hero(Character):
    def __init__(self, weapon, name, power, health):
        self.weapon = weapon
        super(Hero, self).__init__(name, power, health)


alina = Hero("pink gun", "alina", 3, 100)
# alina.name >> woudlnt work, you have to initialize in your child class

# after line 288 now it should work
print(alina.power)
