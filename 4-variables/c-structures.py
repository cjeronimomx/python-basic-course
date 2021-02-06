# tuple

server = ("vm001", "192.168.0.1", "apache-frontend", 5, 8.5, True)
print(server)
len(server)
print(server[1])
server[1] = '10.0.0.1'
print(server.count(5))

# list
servers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
type(servers)
servers[2]
servers[:2]
servers[2:]
servers[10] = 11
    # Use servers whit . operator

    # Uso de pilas
servers.append(0)
popped_item = servers.pop()
print(popped_item)
popped_item = servers.pop(0) # default -1
print(popped_item)

    # Uso de colas
from collections import deque
cola = deque(servers)
type(cola)
cola.append(0)
cola.pop()
cola.popleft()

# set
vowels = {'a', 'e', 'i', 'o', 'u'}
duplicate = {'a', 'e', 'i', 'o', 'u', 'a'}

# dict
server1 = {'name': 'vm004', 'ip': '192.168.0.2', 'ram': 5.5, 'cpu_cores': 8, 'running': True}
type(server1)
server1.keys()
server1.values()
server1.items()
print(server1['ip'])
server1['alias'] = 'tomcat-backend'
server1['running'] = False


# instance
my_instance = set()
type(my_instance)
my_instance.add('a')


# ** Obten las letras del abecesadario de manera ordenada que se encuentra en un texto
# Usando solo estructuras de datos
text = 'obten las letras del abecedario de manera ordenada que se encuentra en un texto'
alphabet = set(text)
alphabet = list(alphabet)
alphabet.sort()
alphabet.reverse()
