def decorator(func):
    def wraper(*args, **kwargs):
        print("==========")
        func(*args, **kwargs)
        print("==========")
    return wraper


@decorator
def test_function():
    try:
        print("New function")
    except Exception as e:
        print(type(e), e)

test_function()