def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend / divisor

def calculate(*values, operator):
    return operator(*values)

result = calculate(50.5, 20.5, operator=divide)

print(result)