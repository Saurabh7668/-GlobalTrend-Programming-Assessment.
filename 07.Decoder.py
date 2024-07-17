Question_7 = """
Write a Python decorator that measures the execution time of a function and logs it. Apply this decorator to a function that performs a computationally expensive task.
"""

import time
import logging

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO)

def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result
    return wrapper

@time_logger
def expensive_computation(n):
    result = 0
    for i in range(n):
        result += i ** 2
    return result

# Example usage:
n = 10**6
result = expensive_computation(n)
print(f"Result of expensive computation: {result}")
