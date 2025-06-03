# Q: Write a decorator that measures the time a function takes to executes.

n = int(input("Enter the time in seconds: "))

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        total = end-start
        print(f"{func.__name__} ran in {round(total, 3)} seconds")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(n)
