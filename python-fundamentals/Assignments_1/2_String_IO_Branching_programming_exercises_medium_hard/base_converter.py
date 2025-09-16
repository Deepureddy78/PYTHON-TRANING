'''3. Base Converter
Description: Read a number and a target base (2, 8, 16), then output the converted number.
Example Input:
Enter number: 42
Enter base: 2
Expected Output:
Binary: 101010
'''

digits= "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def calc(num,base):
    output=''
    if num==0:
        return 0
    while num:
        rem=num%base
        output=digits[rem]+output
        num=num//base
    return output

def main():
    num=int(input("Enter number:"))
    base=int(input("Enter base:"))

    if base==2:
        print("Binary",calc(num,base))
    elif base==8:
        print("Octal",calc(num,base))
    elif base==16:
        print("Hexadecimal",calc(num,base))

if __name__ == '__main__':
    main()