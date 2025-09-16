'''Exercise 5: Truncate Float
Truncate a float to 2 decimal places without round().
Example:
Input: 3.14159
Output: 3.14
'''

def truncate_float():
    num=float(input("Enter number:"))
    num=int(num*100)
    num=num/100
    print(num)


def main():
    truncate_float()

if __name__ == '__main__':
    main()