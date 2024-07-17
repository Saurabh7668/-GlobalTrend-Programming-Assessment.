Question_8 = """
Write a Python function that takes two numbers and an operator (as a string) and performs the corresponding arithmetic operation (addition, subtraction, multiplication, or division).
"""

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operator. Please use '+', '-', '*', or '/'."
        
print(calculate(12, 3, "+"))
print(calculate(12, 3, "-"))
print(calculate(12, 3, "*"))
print(calculate(12, 0, "/"))
print(calculate(12, 3, "^"))
    


            

