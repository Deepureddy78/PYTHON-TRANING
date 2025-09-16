'''
3. Find All Substrings of a String
Description: Generate all possible substrings of a given string. A substring is any continuous part
of the string.
Example Input:
Enter a string: abc
Expected Output:
Substrings: a, ab, abc, b, bc, c
'''

def substring_of_str():
    str=input("enter a string:")
    lst=[]
    s=''
    for i in range(0,len(str)):
        lst.append(str[i])
        # print(str[i])
        for j in range(i+1,len(str)):
            # print(str[i:j+1])
            lst.append(str[i:j+1])
    return lst

def main():
    lst=substring_of_str()
    print(f'Substrings:{','.join(lst)}')

if __name__ == '__main__':
    main()