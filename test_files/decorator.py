def dec_fun(func):
    def wrapper():
        print("the begining")
        func()
        print("wrapper done")
    return wrapper

@dec_fun
def dec_me():
    print("decorate me")


dec_me()


def new_decorator(func):
    def wrap_func():
        print("code before func!")
        func()
        print("code after func!")
    return wrap_func

@new_decorator
def decorate_me():
    print("decorate me!")


decorate_me()