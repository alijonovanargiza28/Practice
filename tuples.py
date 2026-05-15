'''Tuples
1. What is tuple: type vs list
2. Unpacing arguments
3. Zip
'''

print("===What is tuple: type vs list===")
#litral
numbs = [3,5,2,1]

#constructor
letters = list("Hello world")
fruits = ["apple", "lemon", "banan", "kiwi"]
print("before fruits", fruits)

fruits[2]="Melon"

print("after fruits", fruits)

#tuple
animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("abs", 100, True, None)

print(animals[0])
print(animals)

#try aviod this
people = "Diana"
animals = "dog",


print("===Unpacing arguments===")

groups = ["MIT", "FLEXY", "DEVEX", "MG"]
(x, y, *z)=groups
print(f"the X: {x} the Y: {y} the Z: {z} ")
print("z", z)

# * args > tuple
def calculate(*args):
    print("args >", args)
    total = 1
    for x in args:
        total *= x
    print(f"The type(args) value: {type(args)}")
    print(f"The total value: {total}")
    return total

calculate(1,7,2,3)
print("--------")
calculate(0,2,300)
print("--------")
calculate(5,7)

print("--------------")
# **kwargs > dictionary
def intruduce(**kwargs):
    print(f"the type(**kwargs) value:{type(kwargs)}")
    print(f"hi i am {kwargs["name"]} and I am {kwargs["age"]}years old")
    
# call
intruduce(name="Diana", age=22)
intruduce(name="Shawn", age=25, single=True)

print("------------")

def greeting(*args, **kwargs):
    print("*args  >", args)
    print("**kvargs  >", kwargs)

greeting("Hi", True, 20, name="Diana", age = 22)

print("-----ZIP-------")
tuple1 = (1, 2, 3, 4)
tuple2 =('a', 'b', 'c')

zipped = zip(tuple1, tuple2)
print("zipped", zipped)
result = list(zipped)
print(f"the result:{result}")