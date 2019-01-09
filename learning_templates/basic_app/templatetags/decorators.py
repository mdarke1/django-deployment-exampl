def new_decorator(func):

    def wrap_func():
        print("Code here before executing func")
        func()
        print("Func has been called")

    return wrap_func()

def func_needs_decorator():
    print("This function needs a decorator")

#func_needs_decorator= new_decorator(func_needs_decorator)

@new_decorator
def func_needs_decorator():
    print("This function needs a decorator")