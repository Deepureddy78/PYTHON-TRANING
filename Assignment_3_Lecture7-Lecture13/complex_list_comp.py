'''
Exercise 5: Complex List Comprehension  
Generate a new list of squares for numbers that are even and >5 using list comprehension. 
Example:  
Input: [2,4,6,7,8]  
Output: [36,64]
'''

def complex_list_comp():
    lst=list(input("Input:").split())
    lst=[int(num) for num in lst]
    print("Original list: ",lst)
    res=[num**2 for num in lst if num%2==0 and num>5]
    print(list(res))

def  main():
    complex_list_comp()

if __name__ == '__main__':
    main()