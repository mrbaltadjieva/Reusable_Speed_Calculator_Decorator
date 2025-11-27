import time
import functools

def speed_calc_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"Function '{func.__name__}' took {duration:.6f} seconds.")
        return result
    return wrapper

if __name__ == '__main__':
    @speed_calc_decorator
    def fast_function():
        for i in range(1000000):
            i * i
    @speed_calc_decorator
    def slow_function():
        for i in range(10000000):
            i * i

    print("--- Running Speed Tests ---")
    fast_function()
    slow_function()
    print("--- Tests Complete ---")
