'''
Exercise 1: Function as Object Registry  
Create a calculator where operations are stored as functions in a dictionary. Demonstrate 
calling functions dynamically by mapping operation names to functions. 
Example: 
Input: op='add', a=3, b=5  
Output: 8 
'''
def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def mul(a,b):
    print(a*b)

def div(a,b):
    print(a/b)

def mod(a,b):
    print(a%b)

def main():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    op=input("Enter the operation you want to perform(add,sub,mul,div,mod)")

    operations = {
        'add': add,
        'sub':sub,
        'mul':mul,
        'div':div,
        'mod':mod,
    }

    if op in operations:
        operations[op](a, b)
    else:
        print("Invalid operation!")

if __name__ == '__main__':
    main()
