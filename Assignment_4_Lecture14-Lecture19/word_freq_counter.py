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