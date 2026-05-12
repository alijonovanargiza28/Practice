print("== What is Object ==")

import array
import math
import array 
from math import ceil

print(type("hello world"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

#Paradigms
#OOP 4 CONCEPTS > Abstraction | Encapsulation| Inheritencer | Polimorphism
result = math.ceil(97.7) #CALL
print(result)

result2 = ceil(98.7)
print(result2)

print("===Error handling system===")
car_dict = dict(name="Tayota", year=2026, electric=True)

try:
    print("passed here")
    a = car_dict.speed
    result = car_dict["origin"]
    print(result)

except KeyError as err:
   print("No origin state property found:", err)

except AttributeError as err:
    print("no speed  found:", err)

else:
    print("Executed successfuly without errors")
finally:
    print("Final closing logic")