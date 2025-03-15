my_num1 = int (input('Enter firstNumber:')) 
my_num2 = int (input('Enter secondNumber:'))
my_operand = input('Enter operation:')

def my_calculator(a, b, c):
    if c == '+':
        return f"{a} {c} {b} = {a + b}"
    elif c == "-":
        return f"{a} {c} {b} = {a - b}"
    elif c == "*":
        return f"{a} {c} {b} = {a * b}"
    elif c == "/":
        if b != 0:
            return f"{a} {c} {b} = {a / b}"
        else:
            return "Error! Division by zero is not allowed."
    else:
        return "Invalid operator! Please use +, -, *, or /."

print(my_calculator(my_num1, my_num2, my_operand))
