# print("==========")
# count = 0
# while True:
#     count += 1
#     x = int(input("find number"))

#     if x == 41:
#         print(f"You found number in {count} steps")
#         break
#     else:
#         print("Wrong!! please find again!")

print("=== TUPLE ===")

numbs = [3,5,1,2]
print(numbs)

letters = list("Hello world")
print(letters)

fruits = ["apple", "lemon", "banana", "kiwi"]
print("before fruits:", fruits)

fruits[2] = "melon"
print("before", fruits)

cars = ["BMW", "Jip", "Gelik","genesis"]
cars[0]= "Trasker"
print(cars)

animals = ("dog", "cat", "fish", "leon")

tuple_obj =("abs", 100, True, None)

groups = ["Mit", 'Flexy', "devex","MG"]
(x,y, *z) = groups
print(f"x:{x}, y:{y}, z{z}")

def calculate(*args):
    print("args", args)
    total = 1
    for x in args:
        total *= x
    print(f"type(args)value:{type(args)}")
    print(f"the total value:{total}")
    return total

calculate(1,7,3)
calculate(3,7,9)

def introduce(**kwargs):
    print(f"the type(**kwargs) value: {type(kwargs)}")
    print(f"Hi i am {kwargs["name"]} and I am {kwargs["age"]}years old ")

introduce(name = "Diana", age =22)
introduce(name = "Davron", age = 27, single=True)

print("=========zip===========")
tuple1 = (1,2,3,4)
tuple2 = ("a", "b", "c", "d", "e")

zipped = zip(tuple1,tuple2)
print("zipped", zipped)
result = list(zipped)
print(f"the result", result)