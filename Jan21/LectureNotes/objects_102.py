# 3 main problems with structured programming

# 1. emphasis on functionality not data
# 2. Limitations
# 3. Gap in developer client comunication


# Object oriented Programming

#-Objects, classes, abstraction, encapsulation, inheritance, polymorphism

# objects - way to represent real life
#attributes = properties
#behavior - functionality

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

class Student:
    # def __init__(self, name):
    def __init__(self, name, lname):
        self.name = name
        # ^ called an instance variable
        self.lname = lname


student1 = Student("daniela", "arroyo")
# alina = Student("alina")
# joe = Student("joe")

print(student1.name)
print(student1.lname)
# still prints daniela, just for clear understanding on my part
# print(alina.name)
# print(joe.name)
