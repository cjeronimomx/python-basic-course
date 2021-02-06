# int
cpu_cores = 4
print("Número Entero: ", type(cpu_cores))
print(cpu_cores.bit_length())


# float
ram_memory = 4.8
print("Número con punto Decimal: ", type(ram_memory))


# str
host_name = 'vm001'
print("Texto: ", type(host_name))

host_ip = "192.168.0.1"
print("Texto: ", type(host_name))

host_alias = "'jboss-backend'"
print("Texto: ", type(host_name))

# bool
is_running = True
print("Booleano: ", type(is_running))


## Intercambia tipos de datos en variable con tipo diferente

## Prueba parseo de tipos de datos

## Prueba tipos de concatenado de String
print(host_name + "(" + host_alias + ")")
print("{} ( {} )".format(host_name, host_alias))
print("{0} ( {1} )".format(host_name, host_alias))
print("{host_name} ( {host_alias} )".format(host_name=host_name, host_alias=host_alias))
print("The result is: {r:10.2f}".format(r=100/777))
print(f"{host_name} ( {host_alias} )")

## Prueba string multilinea
print("""This is a multilinea
      String""")

## Prueba métodos de string
print('Hello world!'.split())
print(host_ip.split('.'))

course_name = "Python Basic"
print(course_name.find('a'))
print(course_name.find('a', 5))
print(course_name.find('a', 5, 8))

print(course_name.index('Z'))

student_name = 'Crisanto Jeronimo Garcia'
print(student_name.replace('Jeronimo', 'Jerónimo'))
print(student_name.replace('a', 'e'))
print(student_name.replace('a', 'Z', 1))

text_with_spaces = ' This is my text '
print(text_with_spaces.strip())  # lstrip or rstrip

print(student_name.capitalize())
print(student_name.lower())
print(student_name.upper())

print(len(course_name))

print(course_name.count('p'))
print(course_name.count('P'))

## Prueba índices en string
file_system = '/System/Volumes/Data/home'
file_system_permission = 'drwxr-xr--'

print(file_system_permission[3])
print(file_system_permission[-7])

## Prueba slicing en string

print(file_system_permission[:4])
print(file_system_permission[4:])
print(file_system_permission[4:7])

print(file_system_permission[:-4])

## Prueba inmutabilidad
print(host_ip[-1])

host_ip[-1] = '2'