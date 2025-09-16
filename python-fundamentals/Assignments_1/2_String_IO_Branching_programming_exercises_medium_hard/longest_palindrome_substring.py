'''
8. Longest Palindromic Substring
Description: Find the longest substring of a string that is a palindrome.
Example Input:
Enter string: babad
Expected Output:
Longest palindromic substring: bab
'''

def long_palin():
    str=input("enter a string:")
    longest=""
    for i in range(0,len(str)):
        for j in range(i+1,len(str)):
            substr=str[i:j+1]
            if substr==substr[::-1] and len(substr)>len(longest):
                longest =substr
    return longest

def main():
    print(long_palin())

if __name__ == '__main__':
    main()
