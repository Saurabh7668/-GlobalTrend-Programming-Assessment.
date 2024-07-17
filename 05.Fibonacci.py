Question_1 = """
            Write a Python function to compute the nth Fibonacci number using recursion.
"""

def fibo(n):
    if n <= 0:
        print([])

    elif n == 1:
        print(0)
    elif n == 2:
        print(0, 1)

    fib_series = [0, 1]

    for i in range(2, n):
        next_item = fib_series[-1] + fib_series[-2]
        fib_series.append(next_item)

    return fib_series

n = 10
print(f"fabinacci series up to {n} items: {fibo(n)} ")