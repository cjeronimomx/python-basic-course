# while
while True:
    print("This is an infinity loop")

while False:
    print("This message is never printed")


x = 0
while x < 10:
    print(f"Number: {x}")
    x+=1

x = 0
while x < 10:
    print(f"Number: {x}")
    x+=1
else:
    print("Loop is finished")

# ITERA UN SET CON WHILE




# for
vowels = ['a', 'e', 'i', 'o', 'u']
for vowel in vowels:
    print(vowel)

for vowel in vowels:
    print("Iterating with for")

for _ in vowels:
    print("Iterating with for")

for letter in 'Hello world!':
    print(letter)

for index, letter in enumerate('Hello world!'):
    print(f"Letter {index}: {letter}")

names = [('Crisanto', 'Jeronimo', 'Garcia'), ('Juan', 'Lopez', 'Perez')]
for name in names:
    print(name)

for name, first_name, last_name in names:
    print(name, first_name, last_name)


# MODIFICA CADA LETRA EN UNA LISTA POR SU CORRESPONDIENTE ASCCI
ord('a')
chr(97)

# ITERA e IMPRIME LOS VALORES(No Keys) DE UN DICCIONARIO

# CREA UN ARREGLO DE LETRAS A PARTIR DE UN STRING EN UNA SOLA INSTRUCCION
letters = [letter for letter in 'Hello world']


# range
numbers_range = range(100)
for number in numbers_range:
    print(number)

numbers_range = range(10, 20)
for number in numbers_range:
    print(number)

numbers_range = range(10, 20, 2)
for number in numbers_range:
    print(number)

# CREA UN SET DEL ABECEDARIO USANDO FOR y range y en una sola INSTRUCCION
alphabet = [chr(letter) for letter in range(97, 123)]



# pass
for x in range(10):
    pass

# continue
for x in range(10):
    if x%2 != 0:
        continue
    else:
        print(f"Number= {x}")


# break
for x in range(10):
    if x > 5:
        break
    print(f"Number= {x}")
