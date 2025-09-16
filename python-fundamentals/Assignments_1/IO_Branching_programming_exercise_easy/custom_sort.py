'''
4. Custom Sorting
Description: Take a sentence and sort its words by length. If two words have the same length, sort
alphabetically.
Example Input:
Enter a sentence: The quick brown fox jumps over the lazy dog
Expected Output:
Sorted words: dog, fox, the, lazy, over, quick, brown, jumps
'''

def custom_sort():
    str= input("Enter a sentence:-").lower()
    lst=str.split()
    sorted_lst=sorted(lst)
    result=', '.join(sorted(sorted_lst,key=len))
    print("Sorted words: ",result)
    # print(sorted(sorted_lst,key=len))

def main():
    custom_sort()

if __name__ == '__main__':
    main()