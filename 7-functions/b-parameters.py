# Llama función sin argumentos
def func_add(number1, number2):
    print(number1 + number2)

function_a()

# Llama función con argumentos
func_add(2, 4)

# Función con parámetros opcionales
def func_subtract(number1, number2=0):
    print(number1 - number2)

func_subtract(5)
func_subtract(5-2)

# Llama función especificando nombre de parámetro
func_subtract(number1=10, number2=3)
func_subtract(number2=10, number1=1)



# Paso por valor de tipo de dato simple
def func_counter(number=0):
    number += 1
    message = f"The result is: {number}"
    print(message)

num = 1
func_counter(num)
print(num)


# Paso por valor de dato tipo estructura
def modify_list(numbers):
    numbers[0] = 10
    print(f"List modified: {numbers}")

numbers = [0, 1, 2, 3, 4, 5]
modify_list(numbers)
print(numbers)

# Implementa una función que imprima la tabla de multiplicar de N
# Donde N se >0 y <= 10