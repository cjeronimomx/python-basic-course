from subpackage import module_a, module_b

def call_functions():
    module_a.fn_module_a()
    module_b.fn_module_b()


if __name__ == "__main__":
    print("Main module is the entrypoint")
    call_functions()
else:
    print("Main module has been imported")
