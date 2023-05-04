import time
def funcname_time(func):
    def wraper(*args, **kwargs):
        current_time = time.strftime("%H:%M:%S")
        typefunc = type(func)
        func(*args, **kwargs)
        print(f"Function name: {typefunc}, time: {current_time}")
    return wraper

@funcname_time
def my_func(a, b):
    print(a + b)

my_func(1, 2)