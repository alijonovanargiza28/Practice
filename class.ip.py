'''Class deep diving
1. ENCAPSULATION
2. INHERITENCE
3. POLIMORPHISM
'''
print("==INHERITENCE==")
# PARENT => CHILD

class Animal: #Parent
    #state
    description ="The class is perent for Animall"

    #constructor
    def __init__(self, voice):
        self._status ="animal is alive"
        self.voice = voice

    #method
    def make_voice(self):
        print(f"The animal can make voice:{self.voice}")

class Dog(Animal):
    #state

     #constructor
     def __init__(self, name, sound, voice):
         self.name = name
         self.sound = sound
         super().__init__(voice)

      #method
     def make_voice(self):
        print(f"The {self.name} says {self.sound}")

     def introduce(self):
         print(f"{self.name} says: {self.sound} - {self.sound}")
     def protect(self):
         print("Yes I can protact")

class Cat(Animal):
    #state

     #constructor
     def __init__(self, name, sound, voice):
         self.name = name
         self.sound = sound
         super().__init__(voice)

      #method
     def introduce(self):
         print(f"{self.name} says: {self.sound} - {self.sound}")
     def play(self):
         print("I can play with you")

class Fish(Animal):
    #state

     #constructor
     def __init__(self, name, sound, voice):
         self.name = name
         self.sound = sound
         super().__init__(voice)

      #method
     def introduce(self):
         print(f"{self.name} says: {self.sound} - {self.sound}")
     def play(self):
         print("I can swim")
         

dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "zzz", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("-----")
dog.make_voice()
fish.make_voice()
cat.make_voice()

print("----")
print(Animal.description)
print(Dog.description)

print(dog.voice, fish.voice)
print("dog.status:", dog._status)
print("cat.status:", cat._status)

print("==POLIMORPHISM==")
dog.make_voice()
fish.make_voice()

print("------")
# fish > Fish > Animal > OBJECT
a = isinstance(fish, Fish)
c = isinstance(fish, object)
b = isinstance(fish, Animal)
result = a and c and b
print(f"the result: {result}")

#Fish > Animal > Object
data1 = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print("data:", data1, data2)
