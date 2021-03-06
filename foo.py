import time

def foo(func):
    def inner(*arg):
        return func.func_name+": "+str(arg)
    return inner

def run(func):
    def inner(*arg):
        start = time.time()
        func(*arg)
        end = time.time()
        return "time spent: " + str(start - end)

@run
@args
def add(a, b):
    return a + b

print add(500, 1000)
