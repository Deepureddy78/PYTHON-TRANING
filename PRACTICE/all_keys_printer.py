'''
1. All Keys Printer (Recursion on Non-numerics)

Task: Given a nested dictionary, print all keys.
Input:
data = {"a": {"b": {"c": {}}, "d": {}}, "e": {}}
print_keys(data)
Expected Output:
a
b
c
d
e
'''

def all_keys_printer(data):
    for key,value in data.items():
        print(key)
        if isinstance(value,dict):
            all_keys_printer(value)

def main():
    data = {"a": {"b": {"c": {}}, "d": {}}, "e": {}}
    all_keys_printer(data)
if __name__ == '__main__':
    main()