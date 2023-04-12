class MyCustomException(Exception):
    pass


raise MyCustomException("Custom exception is occurred")



try:
    raise MyCustomException("Test")
except MyCustomException:
    print("Custom exception is occurred")