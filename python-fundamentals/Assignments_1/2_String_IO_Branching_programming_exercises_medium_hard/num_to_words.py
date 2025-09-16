'''
13. Number to Words Converter
 Description: Convert a number into words.
 Example Input:
 Enter number: 1234
 Expected Output:
 one thousand two hundred thirty four
'''

def number_to_words():
    ones=["","one","two", "three", "four", "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen"]
    
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    number = int(input("Enter number: "))

    if number ==0:
        print("zero")
        return
    
    words=''

    if number >= 1000:
        if number//1000<20:
            words += ones[number // 1000] + " thousand "
            number %= 1000
    
    if number >= 100:
        words += ones[number // 100] + " hundred "
        number %= 100
    
    if number >= 20:
        words += tens[number // 10] + " "
        number %= 10
    
    if number > 0:
        words += ones[number] + " "
    
    print(words.strip())
    
def main():
    number_to_words()

if __name__ == '__main__':
    main()