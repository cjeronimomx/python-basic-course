# Funciones anidadas
def fn_nested():
    print("Main function")

    def nested():
        print("Nested function")
#fn_nested()


def fn_nested():
    print("Main function")

    def fn_v1():
        print("Nested function v1")
    fn_v1()
#fn_nested()
#fn_v1()


def fn_nested():
    print("Main function")

    def fn_v1():
        print("Nested function v1")
    return fn_v1

func_nested = fn_nested()
print(type(func_nested))
func_nested()





# Decorando una función usando funciones
def fn_decorator(func):
    def fn_wrapper():
        print("**  =====================  **")
        print("\t " + func())
        print("**  =====================  ** ")
    return fn_wrapper


def fn_decorated():
    return "Python Course"


func_decorated = fn_decorator(fn_decorated)
print(type(func_decorated))
func_decorated()





# Decorando función con Decorador
@fn_decorator
def fn_decorated():
    return "Python Course"

fn_decorated()
