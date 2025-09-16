''' 15. Enhanced Calculator
 Description: Calculator supporting +, -, *, /, ^, %, with error handling for invalid inputs.
 Example Input:
 Enter: 5 ^ 3
 Expected Output:
 Result: 125'''

def enhanced_calculator():
    expr = input("Enter: ").strip()
    tokens = expr.split()

    if len(tokens) != 3:
        return "Error: Input must be in the format: number operator number"

    num1_str, op, num2_str = tokens

    # # Validate numbers (integers, decimals, or negative numbers)
    # def is_valid_number(s):
    #     if s.startswith('-'):
    #         s = s[1:]
    #     return s.replace('.', '', 1).isdigit() and s.count('.') <= 1

    # if not (is_valid_number(num1_str) and is_valid_number(num2_str)):
    #     return "Error: Invalid number input"

    num1 = float(num1_str)
    num2 = float(num2_str)

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            return "Error: Division by zero"
        result = num1 / num2
    elif op == '^':
        result = num1 ** num2
    elif op == '%':
        if num2 == 0:
            return "Error: Modulus by zero"
        result = num1 % num2
    else:
        return f"Error: Unsupported operator '{op}'"

    if result == int(result):
        return f"Result: {int(result)}"
    else:
        return f"Result: {result}"

def main():
    print(enhanced_calculator())

if __name__ == '__main__':
    main()