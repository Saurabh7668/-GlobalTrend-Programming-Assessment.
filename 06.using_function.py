def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    return result

# Example usage:
num1 = 10
num2 = 0

print(safe_divide(num1, num2))  # Output: Error: Division by zero is not allowed.
print(safe_divide(num1, 2))     # Output: 5.0
