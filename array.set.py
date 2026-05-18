print("=== Array === ")

from array import array
numbers = array("i", [2,3,4,1,7,9,89,5])

print("Result1", numbers)
numbers.append(100)
numbers.insert(0, 14)
print("Result", numbers)

numbers.remove(5)
numbers.pop()
print(numbers)

del numbers[0:4]
print("numbers", numbers)

print("=== Set === ")
# set unique collection without keeping order!
new_numbers = array("i",[1,7,9,9,9,7,5,6,5,5])
numbs_set = set(new_numbers)

print("numbs_set", numbs_set)

numbs_set.add(200)
print("numbs_set", numbs_set)

numbs_set.add(5)
print("numbs_set", numbs_set)

print("===spesific operators===")
a = {10,20,50,9}
b = {20,10}


result = a|b
result2 = a & b
result3 = a - b
result4 = a^b

print(result)
print(result2)
print(result3)
print(result4)



 