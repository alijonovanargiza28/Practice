print("==Iterable objects & Range===")

text = "MIT"
for letter in text:
    print(f"the letter:{letter}")

range_obj = range(3)
print("range_obj", range_obj)
for ele in range_obj:
    print(f"the letter: {ele}")


print("===DICTIONARY===")
person ={"name":"Diana","age":22,"single":True}
person_obj = dict(name="Diana", age=22, single=True)
print(f"The person{person}")
print(f"The person{person_obj}")

name = person_obj.get("name")
hobby = person_obj.get("hobby")
balance = person_obj.get("balance", 10)
name = person_obj["name"]
print(f"name:", name)
print(f"The name:{name} hobby: {hobby} balance is {balance}")

for key in person_obj:
    print(f"the key: {key}")

del person_obj["single"]
for key in person_obj:
    print(f"the key:{key}=> value {person_obj.get(key)}")