def decorator_function(func):
    def wrapper_function(*args, **kwargs):
        print(f"Function name: {func.__name__}")
        if args:
            print(f"Positional arguments: {args}")
        if kwargs:
            print(f"Keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"result: {result}")
        print("\n")
        return result
    return wrapper_function

@decorator_function
def greet(name, age, country):
    print(f"Hello, {name}, you are {age} years old and from {country}.")
@decorator_function
def sum_numbers(a, b):
    return a + b
@decorator_function
def multiply_and_sum(*args, factor):
    total = sum(args)
    return total * factor

greet("Alice", 30, "USA")
sum_numbers(5, 10)
multiply_and_sum(1, 2, 3, factor=2)