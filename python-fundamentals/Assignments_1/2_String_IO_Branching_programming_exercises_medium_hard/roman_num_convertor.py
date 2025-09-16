''''
9. Roman Numeral Converter
Description: Convert a number (1–3999) into Roman numerals.
Example Input:
Enter number: 1994
Expected Output:
Roman numeral: MCMXCIV
'''

def number_to_roman():
    roman_numerals = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"),  (90, "XC"), (50, "L"),  (40, "XL"),
        (10, "X"),   (9, "IX"),  (5, "V"),   (4, "IV"), (1, "I")
    ]

    number = int(input("Enter number: "))

    if number < 1 or number > 3999:
        print("Number out of range (must be 1–3999).")
        return

    result = ""
    for value, symbol in roman_numerals:
        while number >= value:
            result += symbol
            number -= value

    print("Roman numeral:", result)

def main():
    number_to_roman()

if __name__ == '__main__':
    main()
