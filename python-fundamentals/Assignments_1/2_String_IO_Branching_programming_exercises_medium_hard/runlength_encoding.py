'''1. Run-Length Encoding
Description: Compress a string using run-length encoding. Example: 'aaabbcddd' → 'a3b2c1d3'.
Handle both uppercase/lowercase.
Example Input:
Enter a string: aaabbcddd
Expected Output:
Encoded string: a3b2c1d3
'''
def runlength_encoding():
    string = input("Enter a string: ")
    output = ''
    check_list = []

    for char in string:
        if char not in check_list:
            count = string.count(char)
            output = output +( char + str(count))
            check_list.append(char)
    return output

def main():
    print("Encoded string:", runlength_encoding())

if __name__ == '__main__':
    main()