'''Loop operators
1. for
2. break/else
3. while
'''
print("===for operators===")

text = "MIT"

for letter in text:
    print(f"The letter: {letter}")

numbs = [10,7,3,4]
for number in numbs:
        print(f"the number:{number}")

car_obj = dict(brand="Ferrari", year=2026)
for car in car_obj:
     print(f"The car {car_obj}")

print("-----------------")

for key in car_obj:
      print(f"Key: {key} => value: {car_obj.get(key)}")


range_obj = range(5)

for x in range_obj:
     print(f"the element:{x}")


for x in range(1,20,5):
      print(f"the x: {x}")


print("===Break/else===")
for x in range( 1, 20, 5):
      print(f"the x {x}")
      if x > 10:
            print("Reached break")
            break
else:
      print("Looped successfully")


print("== White operators ==")

numb = 40
while numb > 0:
      numb -=10
      print(f"the number {numb}")

print("===")
count = 0
while True:
      count += 1
      x = int(input("O`ylagan raqamimni kiriting"))
     
      if x == 41:
            print(f"siz raqamni {count} urunishda topdingiz")
            break
      else:
            print("Xato! qaytadan urinib ko`ring")
