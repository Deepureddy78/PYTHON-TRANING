'''
10. Text Justifier
Description: Given a sentence and width k, format the text so each line is fully justified.
Example Input:
Sentence: 'This is an example of text justification.'
Width: 16
Expected Output:
This is an
example of text
justification.
'''

def text_justifier():
    sentence = input("Sentence: ").split()
    width = int(input("Width: "))
    
    line = ""
    
    for char in sentence:
        if len(line) + len(char) + 1 <= width:
            if line != "":
                line += " "
            line += char
        else:
            print(line)
            line = char
    
    if line:
        print(line)

def main():
    text_justifier()

if __name__ == '__main__':
    main()