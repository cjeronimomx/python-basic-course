
a = None
print(a)
a = 'a'

b = 'b'
c = a + b

del a
del b, c

_a = 'a'
b2 = 'b2'
c_d = 'c d'


A = 'A'
Text = 'text'


list = list([1, 2])


return = 'a'


# SCOPE GLOBAL/LOCAL/LOCAL CON keywork GLOBAL

def testing(x1):
    global x2
    x2 = 3
    return x1