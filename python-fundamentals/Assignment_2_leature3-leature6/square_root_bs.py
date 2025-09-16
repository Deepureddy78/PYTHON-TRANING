'''
Exercise 6: Square Root Binary Search
Find integer square root using binary search.
Example:
Input: 17
Output: 4
'''

def square_root():
    num=int(input("Enter a number: "))

    if num < 0:
        print("Negative numbers don't have real square roots.")
        return None
    
    if num == 0 or num == 1:
        return num
    
    start=0
    end=num
    res=0

    while start<=end:
        mid=(start+end)//2
        if mid*mid == num:
            return mid
        elif mid*mid < num:
            res=mid
            start=mid+1
        elif mid*mid > num:
            end=mid-1
    return res

def main():
    res=square_root()
    print(res)

if __name__ == '__main__':
    main()