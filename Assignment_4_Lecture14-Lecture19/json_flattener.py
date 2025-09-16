'''
9. JSON Flattener (Recursion + Dictionaries)
Task: Flatten nested dictionaries.
Input:
data = {"user": {"name": "Alice", "address": {"city": "Paris", "zipcode": 75000}}}
Expected Output:
{"user.name": "Alice", "user.address.city": "Paris", "user.address.zipcode": 75000}
'''
data = {
    "user":{
        "name": "Alice", 
        "address": {
            "city": "Paris",
             "zipcode": 75000
        }
        
    }
}
output={}

def flattener(data, prefix=""):
    for key,value in data.items():
        new_prefix = prefix+"."+key if prefix else key
        if isinstance(value, dict):
            flattener(value, new_prefix)
        else:
            output[new_prefix] = value

def main():
    flattener(data)
    print(output)

if __name__ == '__main__':
    main()