'''
Exercise 3: Immutable vs Mutable 
Show that tuples cannot be modified by trying to append an item. Then contrast with lists 
which can be updated.  
Example:  
Input:  
tuple=(1,2,3), try append(4)  
Output: Error  
Input: 
List=[1,2,3], append(4)  
Output: [1,2,3,4] 
'''

def check_mutabality():
    tuple=(1,2,3)
    print("original tuple0",tuple)
    try:
        tuple.append(10)
    except AttributeError as e:
        print("Error when trying to append to tuple: ",e)

    list = [1,2,3]
    print("original tuple0",tuple)
    list.append(4)
    print("Updated_list",list)
def  main():
    check_mutabality()

if __name__ == '__main__':
    main()