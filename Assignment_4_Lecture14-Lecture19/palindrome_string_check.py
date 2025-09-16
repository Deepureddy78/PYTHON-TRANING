'''
6. Palindromic String Check (Recursion on Non-numerics)
Task: Recursively check if a string is palindrome.
Input:
is_palindrome("racecar")
is_palindrome("hello")
Expected Output:
True
False
'''

def is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

def main():
    print(is_palindrome("racecar")) 
    print(is_palindrome("hello"))    

if __name__ == '__main__':
    main()
