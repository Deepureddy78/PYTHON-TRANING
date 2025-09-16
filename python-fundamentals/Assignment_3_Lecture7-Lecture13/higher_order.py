'''
Exercise 7: Higher-Order Function with Callable Implement  
repeat(func,times,value) to apply a function repeatedly to an initial value.  
Example:  
Input: func=lambda x:x+2, times=3, value=1  
Output: 7  
'''

def repeat(func, times, value):
    for _ in range(times):
        value = func(value)
    return value

def main():
    # Get the lambda function as a string
    func_input = input("Enter a function (e.g., 'lambda x: x + 2'): ")

    # Convert the input string into an actual function using eval
    func = eval(func_input)

    # Get the number of times to apply the function
    times = int(input("Enter number of times to repeat the function: "))

    # Get the initial value
    value = int(input("Enter the initial value: "))

    # Call the repeat function
    result = repeat(func, times, value)

    # Show the result
    print("Result:", result)


if __name__ == '__main__':
    main()