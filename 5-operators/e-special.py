host_ip = '192.168.0.4'

# Is
print(1 is 1)
print((1, 2) is (1, 2))

# Is Not
a = set(['a'])
b = set(['b'])
print(a is not b)
c = a
print(a is c)

# In
print('192' in host_ip)
print('a' in a)
print('b' in a)

colors = {'1': 'red', '2': 'orange', '3': 'blue'}
print('orange' in colors)
print('1' in colors)

# Not In
print('192' not in host_ip)
print('10' not in host_ip)
print('a' not in a)
print('b' not in a)