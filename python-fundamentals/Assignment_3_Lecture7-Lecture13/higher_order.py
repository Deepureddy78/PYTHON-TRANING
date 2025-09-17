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
    func_input = input("Enter a function (e.g., 'lambda x: x + 2'): ")

    func = eval(func_input)
    times = int(input("Enter number of times to repeat the function: "))
    value = int(input("Enter the initial value: "))
    
    result = repeat(func, times, value)
    print("Result:", result)


if __name__ == '__main__':
    main()