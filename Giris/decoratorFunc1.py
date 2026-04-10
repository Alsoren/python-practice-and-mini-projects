#Phyton Decorator Function Giris
def decorator_function(func): # Decorator function - accepting a function as an argument
    def wrapper_function(*args, **kwargs):
        print(f"Start")
        result =func(*args,**kwargs)
        print(f"End")
        return result
    return wrapper_function

@decorator_function # Using the decorator
def myMesage():
    print("this is a example")

myMesage()
