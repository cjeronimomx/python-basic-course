"""
value = input("Enter value: ")
print(type(value))

# Use int(), float(), bool()

while not value.isdigit():
    new_value = input("Enter value: ")
else:
    print(int(new_value))

print(bool(value.capitalize()))
"""


# Python debugger
import pdb

a = 1
b = 2
c = list([1, 2, 3, 4])
# pdb.set_trace()
print(a + b)
# insert debug

# breakpoint() # Write p a or p b+c and q for exit
print(b + c)

