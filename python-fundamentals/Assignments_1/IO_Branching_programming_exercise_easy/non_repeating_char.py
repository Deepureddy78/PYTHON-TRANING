'''
2. First Non-Repeating Character
Description: Find the first character in a string that does not repeat anywhere else. If all characters
repeat, return None.
Example Input:
Enter a string: swiss
Expected Output:
First non-repeating character: w
'''

def non_repeathing_char(str):
    for i in range(0,len(str)):
        if str[i] not in str[i+1:len(str)] and str[i] not in str[0:i-1]:
            return str[i]
            break
    return None
    
def main():
    str=input("Enter a string\n")
    output=non_repeathing_char(str)
    print("First non-repeating character:",output)

if __name__ =="__main__":
    main()