'''
Exercise 6: Copy vs Alias  
Show aliasing by assigning a list to another variable and modifying one. Then show shallow 
copy using slicing to avoid shared changes.  
Example:  
Input: A = [1,2], B=A, B.append(3)  
Output: A=[1,2,3]  
Input: C=A[:], C.append(4)  
Output: A=[1,2,3], C=[1,2,3,4]  
'''
def copy_vs_alis():
    A = [1,2]
    B=A
    B.append(3) 
    print("A",A)

    C=A[:]
    C.append(4)
    print("A",A)
    print("C",C)

def main():
    copy_vs_alis()

if __name__ == '__main__':
    main()
    