'''
Exercise 4: List Mutability Demonstration  
Pass a list into a function that appends a new element. Show how the original list changes 
after the function call.  
Example: 
Input: L=[1,2], call add_three(L)  
Output: [1,2,3]  
'''

def add_three(lst):
    lst.append(3)

def main():
    L = [1, 2]
    print("Before function call:", L)
    
    add_three(L)
    
    print("After function call: ", L)

if __name__ == "__main__":
    main()
