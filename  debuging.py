'''Packages & Debugging
    (1)Python packages & core package
    (2)Package menejer & extarnal package
    (3)Debugging
'''
from PIL import Image
# import turtle
# t = turtle.Turtle()

# t.shape("turtle")
# t.speed(0.5)
# t.circle(100)
# turtle.done()

my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print(content)
finally:
    my_file.close()

with open("material/message.txt", "r") as your_file:
    content = your_file.read()
    print("your file:", content)
print("DONE")


print("===== Package Manager & External Package =====")
''' Package Managers: pip pipenv npm yarn composer brew'''
# External Package > https://pypi.org/
with Image.open("material/image.png") as img_obj:
    resized_img = img_obj. resize((100, 100))
    resized_img.show()
    resized_img.save("material/sample.png")

def summary(*args):
    total = 0
    for x in args:
        total += x
        return total


test = 100
result = summary(1, 2, 3, 4, 5)