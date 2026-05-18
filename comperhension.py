print("==== comprhension ====")
numbers = [2,4,6,4,5,8]
list_numbers = [*numbers]
print("list_numbers", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))

print('---------------')
people = [("Diana", 22), ("Dina", 23), ("Anna", 27)]
list_people =[person[0] for person in people]
print("list_people", list_people)

cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi", 128),
    ("Bmw", 100),
    ("Pagani", 33)
]
list_cars =[car[0] for car in cars if car[1]>80]
print("list_cars", list_cars)

print("-----------")
numbs =[4,6,2,7,9,8,8]
set_numbs ={*numbs}
print(set_numbs)

dict_people = {person[0]: person[1] for person in people}
print("dict_people",dict_people)

dict_people = {person[0]: person[1] for person in people if person[1] > 23}
print("dict_people",dict_people)