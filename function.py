#Function
# (1) DEFINE vs CALL
# (2) Parametr vs Argument
# (3) Keyword & default arguments
# (4) Scope

print("====DEFINE CALL====")
# built in function > print() type()
#Function malum bir mantiqni ishga tushurib beradigan block kod
#Pythonda indentation! :
# pass bosh hech narsa qilma

# Define
def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("Greeting is executed")
    return f"Hi {b}"


#CALL
greet("DIANA")
result = greeting("Martin")
print("Result", result)

print("=== Keyword & default arguments ===")
# Define
def give_great(name,age=22):
    print("give_great is executed")
    return f"Hi {name}, you are {age} years old"

#Call
result1 = give_great(name="Lily", age=20)
print("Result", result1)

result2 = give_great(name="Rose")
print("Result", result2)


print("===Scope===")
b = 100

#DEFINE
def calculate(a,b):
    c = a * b
    print(f"the c value {c}")

#Call
calculate(5,50)


