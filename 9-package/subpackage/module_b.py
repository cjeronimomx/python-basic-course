def fn_module_b():
    print("This is module B")


if __name__ == "__main__":
    print("Module B is the entrypoint")
else:
    print("Module B has been imported")