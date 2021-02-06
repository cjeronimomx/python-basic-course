# Ejemplo función sin valor de retorno
def func_a():
    print("Function with empty return")
    return

a = func_a()
print(type(a))


# Ejemplo de función con retorno simple
def func_b():
    print("Function with return value")
    return "message"

b = func_b()
print(type(b))
print(b)


# Ejemplo de función con retorno tupla
def fn_c():
    return ('a', 'b', 'c')

c = fn_c()
print(c)
print(type(c))


def fn_d():
    return (1, 'x', True)

d1, d2, d3 = fn_d()
print(f"d1={d1} d2={d2} d3={d3}")
print(f"d1={type(d1)} d2={type(d2)} d3={type(d3)}")


# Crea una función que retorne el máximo y el mínimo en una lista de numeros
