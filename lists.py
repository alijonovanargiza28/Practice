'''List
1. working with list
2. list method
3. lambda function
4. enumarate, map and filter
'''
print("=== Working with list ===")
person = {"name": "Diana", "age":22} #dictionary
people = ("Andrew", "John", "Michel") #tuple
groups =["MIT", "Flexy", "Devex", "MG"] #list
for team in groups:
    print(f"the team, {team}")

#constructor
result = list("Hello world!")
print(f"the letter {result} and size: {len(result)}")

print("------")
fruits = ["Apple", "orange", "lemon", "kiwi"]
a = fruits[0]
b = fruits[0:2]
c = fruits[::2]
d = fruits[:: -1]

print("a:", a)
print("b", b)
print("c", c)
print("d",d)

print("--- list methods ---")
# method > append() insert() pop() remove() clear() sort()  index()

letters = ["a","d","b"]

letters.append("c") #add behind
print(f"The append: {letters}")

letters.insert(0, "z") #add front
print(f"the insert result{letters}")

size = len(letters) -1
result = letters.pop(size) #pop behind
print(f"The pop result {result} and letters:{letters}")

result2 = letters.pop(0) #pop front
print(f"the pop result{result2} and letter {letters}")


print("-------------")
animal =["dog", 'cat',"capybara", "fish", "lion"]
print("aminal:", animal)

animal.remove("lion")
print("animals remove", animal)

del animal[2:4]
print("animals delete", animal)

exits = animal.index("cat")
print("cat exist:", exits)

animal.clear()

if "cat" in animal:
    print("index of cat:", animal.index("cat"))
else:
    print("cat does not exist")


print("-----Sort------")
numbers =[2,20,12,8,57]
numbers.sort()
print("numbers:", numbers)
numbers.sort(reverse=True)
print("sort reverse:", numbers)


#immutable
numbs = [2,20,12,100]
new_numbs = sorted(numbs)
print(f"the sorted numbs: {numbs} and new_numbs:{new_numbs}")

print("=== Lambda function ===")
# lambda is small anonymous function
def calculate(x,y):return x * y

result = calculate(3,5)
print("result:", result)

people =[
    ("Diana", 22),
    ("Stave", 25),
    ("Mical", 30),
    ("shawn",32),
    ("Ali", 40)
]
people.sort()
print("people --->", people)

#sort by age via lambda
people.sort(key=lambda person: person[1])
print("people2 --->", people)


print("---enumerate, map and filter----")
# enumerate for index & value

animal =["dog", "cat", "fish", "capybara"]
for element in enumerate(animal):
    print("element:", element)

print("-----------")
for (index, value) in enumerate(animal):
    print(f"the index:{index} value {value}")


#similar in dictionary
car_obj = dict(brand="Ferrari", year = 2015)
result = car_obj.items()
for (key, value) in result:
     print(f"the key:{key} value {value}")


print("=== Map ===")
cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi", 116),
    ("Bmw", 109),
    ("Pagani", 33)
]

result_map = map(lambda car: car[0], cars)
print(f"the result_map {result_map} and types:{type(result_map)}")
new_car = list(result_map)
print("new_car(2)", new_car)

print("===filter===")
result_filter = filter(lambda car: car[1]>80,cars)
print(f"the result_filter: {result_filter} and type: {type(result_filter)}")
print(list(result_filter))
