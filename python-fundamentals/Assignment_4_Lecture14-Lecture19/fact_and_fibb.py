def factorial(num):
    if num ==0 or num==1:
        return 1
    return num*factorial(num-1)

def fibonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    return fibonacci(num-1) + fibonacci(num-2)
    
def main():
    print(factorial(5))
    print(fibonacci(6))

if __name__ == '__main__':
    main()