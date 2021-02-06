def calculator():
    # Atrapa exception lanzada desde otra función
    try:
        operation, number_1, number_2 = read_data()

        if operation == "+":
            add(number_1, number_2)
    except Exception as ex:
       print(ex)

def add(num1, num2):
    pass

def read_data():
    valid_operators = {'+', '-', '*', '/'}
    # 8 Valida valor de operador y lanza exception
    operation = input(f"Enter operator{valid_operators}: ")
    if operation not in valid_operators:
        raise ValueError(f"Invalid operator, valid options: {valid_operators}")

    # 1 Ejecuta programa ingresando letras en lugar de números
    # 2 Agrega try-excep e imprime mensaje
    # 3 Agrega alias a exception
    # 4 Provoca un tipo de exception diferente a la cachada
    # 5 Atrapa una segunda y tercera tipo de exception adicional
    # 6 Agrega else
    # 7 Agrega finally

    try:
        number_1 = int(input("Enter number one: "))
        number_2 = int(input("Enter number two: "))
    except ValueError as ex:
        print(f"Warning: {ex}")
    else:
        print("No Exceptions!!")
    finally:
        print("Always execute this")

    return operation, number_1, number_2


if __name__ == "__main__":
    calculator()


# 10 implementa lectura de valores sin finalizar el programa hasta que se introduzcan datos correctos
# 11 implemente llamda a función diferente de acuerdo al operador introducido