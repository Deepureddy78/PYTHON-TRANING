def armtrong_num(num):
    count=len(str(num))
    n=num
    res=0
    while n:

        res=res+((n%10)**count)
        n=n//10
    return res

def main():
    num=int(input("Input: "))
    res=armtrong_num(num)
    if res==num:
        print(f'{num} is an Armstrong number.')
    else:
        print(f'{num} is not an Armstrong number.')

if __name__ == '__main__':
    main()