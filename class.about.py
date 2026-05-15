'''CLASS
   1. What is class
   2. ordinary vs static properties
   3. special methods
'''

print("== What is class ==")

class Person():
    # state
    message = "class state property"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def intruduce(self):
        print(f"{self.name} says: How do you do!")

    def say_age(self):
        print(f"{self.name} says I am {self.age}")

    @classmethod
    def explain(cls):
        print("static method property executed")


person1 = Person("Diana", 22)
person2 = Person("Martin", 35)

# ordinary state
print("person1.name", person1.name)

# ordinary method
person1.intruduce()
person2.say_age()

print("==")

# static state
new_message = Person.message
print("new_message", new_message)

# class method
Person.explain()

print("=== special/magic methods ===")
#__init__, __new__, __str__, __call__,

class Car():
    #state
    description ="This class makes cars"
    #constructor
    def __init__(self, name, year):
        self.name = name
        self.year = year
    #method
    def start_engine(self):
        print(f"The {self.name} start engine!")

    def stop_engine(self):
        print(f"The {self.name} stopped engine!")

    def __str__(self):
        return f"The car name: {self.name} was prodected in {self.year} year"
    
    def __call__(self):
        print("Object called as function")
        return True
my_car = Car("Ferrari", 2025)
my_car.start_engine()
my_car.stop_engine()

print("====")
your_car = Car("Tayota", 2016)
print(your_car)
your_car()
responce = your_car()
print("response:", responce)