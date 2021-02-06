# Función con args
def fn_args(*args):
    print(f"TYPE: {type(args)}")
    print(f"SIZE: {len(args)}")
    print(f"VALUE: {args}")

fn_args()
fn_args(1)
fn_args('a')
fn_args(('a', 'b', 'c'))
fn_args(1, 'a')


# Función con args más parámetros al final
def fn_args_2(*args, param1, param2):
    print(f"TYPE: {type(args)}")
    print(f"SIZE: {len(args)}")
    print(f"VALUE: {args}")

fn_args_2()
fn_args_2(1, 2)
fn_args_2(param1=1, param2=2)


# Función con args más parámetros al principio(Convención)
def fn_args_3(param1, param2, *args):
    print(f"TYPE: {type(args)}")
    print(f"SIZE: {len(args)}")
    print(f"VALUE: {args}")

fn_args_3()
fn_args_3(1, 2)
fn_args_3(param1=1, param2=2)




#
def fn_kwargs(**kwargs):
    print(f"TYPE: {type(kwargs)}")
    print(f"SIZE: {len(kwargs)}")
    print(f"VALUE: {kwargs}")

fn_kwargs()
fn_kwargs(user='cjeronimo', passwd='admin123')

# Implementa una función que reciba una lista de hostname y un dicionario de servers
# Debe devolver la ip de cada hostname, si no existe un hostname debe devolver None