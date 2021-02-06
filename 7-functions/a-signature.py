# 1 Ejecuta script con función sin llamarla
def function_name():
    pass
print(type(function_name))

def first_function():
    """
    Docstring - Comentario para documentar la función
    """
    print("This my first function")


# 2 Ejecuta script con llamada a función
function_name()

# 3 Ejecuta script con llamda a función en main
if __name__ == "__main__":
    function_name()


# CREA 3 FUNCIONES, SE DEBEN LLAMAR DESDE MAIN
