'''OPERATORS & CONDITIONS
1. Operators
2. Conditions
3. Logical Operators
'''

print("==Operators==")
# + - > >= < <= == is* /  // % += **

a = 19
b = 5

print("a > b", a > b)

result = a // b 
left = a % b
print(f"the result: {result} and left: {left}")

a += 100
print("a:", a)

print("b**2", b**2)
print("b**3", b**3)

print("="*15)

c = dict(name="Diana", age = 22)
d = dict(name="Diana", age = 22)
e = c

print("c==d", c == d) # only value 
print(id(c), id(d))

data = c is d
print("c is d", data)

print("e is d", e is c)

print("==Conditon==")
x = 15

if x > 50:
  print("case A")
elif x > 10:
  print("case B")
else:
  print("case C")

print("===LOgical Operators====")
age = 20
  #Ternary
person = "adult" if age > 18 else "minor"
print("Person:", person)

is_student = True
is_admin = False
is_parent = True
is_gues = True

if not is_student:
  print("Welcome here, do you want to be student")
elif is_admin:
  print("Please go to this office")
elif is_gues or is_parent:
  print("Waiting room is over there")
else:
  print("Other cases")
