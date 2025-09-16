'''2. Word Histogram
Description: Given a paragraph from the user, print a histogram (in text form) showing frequency
of each word.
Example Input:
Enter text: the cat sat on the mat
Expected Output:
Histogram:
the: 2
cat: 1
sat: 1
on: 1
mat: 1
'''
def histogram():
    txt= input("Enter text:").split()
    print("Histogram")
    checked_list=[]
    for char in txt:
        if char not in checked_list:
            print(f"{char}:{txt.count(char)}")
            checked_list.append(char)

def main():
    histogram()

if __name__ == '__main__':
    main()