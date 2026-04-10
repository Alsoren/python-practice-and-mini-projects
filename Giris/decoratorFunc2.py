import time 
def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"function {func.__name__} execution time: {end_time - start_time: .5f} seconds")
        return result
    return wrapper

@time_decorator
def slow_function(n):
    total = sum(range(n))
    print(f"Finished slow function, total: {total}")
@time_decorator
def fast_function(n):
    total = sum(range(n))
    print(f"Finished fast function, total: {total}")
@time_decorator
def faster_function(n):
    total = sum(range(n))
    print(f"Finished faster function, total: {total}")

slow_function(1000000)
fast_function(10000)
faster_function(0)