print("====number====")
# in JAVA variable is a name storage location
# in Python, variable is name reference!

count = 100
count_type = type(count)
#print("count", count, count_type)
print(f"the count: {count} and type:{count_type}")

result4 = count.bit_count() #method
result2 = count.numerator #state
print(result4, result2)

print("====String====")
# Methods: upper() lower() title() find() replace()
course = "AI python fullStack"
result = type(course)
print(f"the type of course:{result}")
result = course.title()
print(f"the resoult: {result}")

print(f"the result(2): {result}")
result = course.upper()

print(f"the result(3): {result}")

result = course.replace("Fullstack" , "MasterClass")
print(f"the result(4): {result}")
print(course)

print("===boolen====")
# function > type() input() bool() int() str()
y = input("Give your value for y:")
print("y:", y)

result = y.isnumeric()
print(f"The input value is numeric: {result}")


#TRUTHY VS FALSY value
#Truthy > True 100 -100 "MIT"
#FALSY > False 0 "" None

test_trusy ="DIANA" and False and 100
print("The Trusy:", bool(test_trusy))

test_falsy =""
print("The Falsy:", bool(test_falsy))

