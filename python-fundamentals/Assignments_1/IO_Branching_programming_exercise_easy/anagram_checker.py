'''
1. Anagram Checker
Description: Check if two given strings are anagrams of each other (contain the same letters in a
different order). Ignore spaces, punctuation, and case.
Example Input:
Enter first word: Listen
Enter second word: Silent
Expected Output:
Yes, they are anagrams.
'''

# char_list = [ 
#     'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
#     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
#     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
#     '0', '1','2','3','4','5','6','7','8','9'
# ]

def check_anagram():
    firstword= (input("Enter first word\n"))
    secondword=sorted(input("Enter second word:\n"))
    f = sorted(''.join(char.lower() for char in firstword if char.isalnum()))
    s = sorted(''.join(char.lower() for char in secondword if char.isalnum()))

    if f == s:
        print("Yes,they are anagram")
    else:
        print("No,they are not anagram")

def main():
    check_anagram()
    
if __name__ == '__main__':
    main()