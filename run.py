# Dunder _builtins_ , _init_
message = ("PYTHON: Everything is object")
print(message)

result = type(message)
print(result)

#In Python thre are builtin tools:
#(1) TYPES > init float str list dict
#(2) Function > print()len()input()type()
#(4) CONSTANTS > True False None

print(dir(__builtins__))