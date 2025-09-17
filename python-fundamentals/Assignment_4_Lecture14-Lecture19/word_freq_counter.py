'''
1. Word Frequency Counter (Dictionaries)
Task: Count word occurrences in a paragraph.
Input:
"the cat sat on the mat with the other cat"
Expected Output:
{'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1, 'with': 1, 'other': 1}
'''

def word_freq_counter():
    dict = {}
    sentence=input("Input: ").split()
    print(sentence)
    for word in sentence:
        if word not in dict:
            dict[word]=1
        else:
            dict[word]+=1
    print(dict)

def main():
    word_freq_counter()

if __name__ == '__main__':
    main()

