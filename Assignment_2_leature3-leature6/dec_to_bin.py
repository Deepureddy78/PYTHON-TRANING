'''
Exercise 3: Decimal to Binary
Convert a decimal number to binary programatically.
Example:
Input: 10
Output: 1010
'''

def dec_to_bin():
    num=int(input("Input: "))
    if num==0:
        print("0")
        return 0
    output=''
    while num>0:
        rem=num%2
        output=str(rem)+output
        num=num//10
    print(output)

def main():
    dec_to_bin()

if __name__ == '__main__':
    main()