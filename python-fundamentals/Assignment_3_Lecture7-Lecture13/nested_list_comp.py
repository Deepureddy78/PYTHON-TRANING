'''
Exercise 10: Nested List Comprehension with Tuples  
From a list of student records, generate tuples of (name, average_grade) using nested list 
comprehension.  
Example: 
Input: [('Alice',[80,90]), ('Bob',[70,100])]  
Output: [('Alice',85.0), ('Bob',85.0)]
'''

def nested_list_comp():
    exp = eval(input("Enter the list\n"))
    res_exp=[(tup[0],sum(tup[1])/len(tup[1])) for tup in exp]
    print(res_exp)

def main():
    nested_list_comp()

if __name__ == '__main__':
    main()