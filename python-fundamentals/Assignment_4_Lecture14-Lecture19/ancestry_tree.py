'''
2. Ancestry Tree Traversal (Recursion on Non-numerics)
Task: Given a nested family dictionary, print all descendants of a person.
Input:
family = {"John": {
                "Alice": {
                    "Sam": {},
                    "Lily": {}
                    },
                    "Bob": {}
                    }
                }
find_descendants("John", family)
Expected Output:
Alice
Sam
Lily
Bob
'''

family = {
    "John": {
        "Alice": {
            "Sam": {}, 
            "Lily": {
                "Karan": {}
            }
        }, 
        "Bob": {}
    }
}

def find_descendants(ancesstor, family, ancesstor_found=False):
    for parent, desc in family.items():
        true_ancesstor = True if parent == ancesstor else False
        if parent != ancesstor and ancesstor_found:
            print(parent)
        find_descendants(ancesstor, desc, ancesstor_found or true_ancesstor)


find_descendants("John", family)