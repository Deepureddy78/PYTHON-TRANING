'''
Exercise 4: Longest Word
Find the longest word in a string.
Example:
Input: 'I love programming'
Output: 'programming'
'''

def longest_word():
    sentence=input("Enter a sentence").split()
    longest_word = sentence[0:1]
    for word in sentence:
        if len(word)>len(longest_word):
            longest_word=word
    print(longest_word)

def main():
    longest_word()

if __name__ =='__main__':
    main()