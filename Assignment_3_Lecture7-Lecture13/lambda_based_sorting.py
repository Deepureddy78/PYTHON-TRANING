'''
Exercise 2: Lambda-Based Sorting
Sort a list of tuples using lambda.
For example, sort by age in descending order.
Example:
Input: [('Alice',25), ('Bob',30), ('Cara',22)]
Output: [('Bob',30), ('Alice',25), ('Cara',22)]
'''

def sorting():
    Input = [('Alice',25), ('Bob',30), ('Cara',22)]
    sorted_list=sorted(Input, key= lambda x:x[1],reverse=True )
    print(sorted_list)

def main():
    sorting()

if __name__ == '__main__':
    main()