def find_descendants(person, family):
    """
    Recursively find and print all descendants of a given person.
    
    Args:
        person (str): The person whose descendants we want to find
        family (dict): Nested dictionary representing the family tree
    """
    # Base case: if person not in family tree, return
    if person not in family:
        return
    
    # Get the children of the current person
    children = family[person]
    
    # Print each child and recursively find their descendants
    for child in children:
        print(child)
        # Recursive call to find descendants of this child
        find_descendants(child, family)


# Test with the provided example
family = {
    "John": {
        "Alice": {
            "Sam": {},
            "Lily": {}
        },
        "Bob": {}
    }
}

print("Descendants of John:")
find_descendants("John", family)

# Additional test cases
print("\nDescendants of Alice:")
find_descendants("Alice", family)

print("\nDescendants of Sam (no descendants):")
find_descendants("Sam", family)

# Example with a more complex family tree
extended_family = {
    "John": {
        "Alice": {
            "Sam": {
                "Emma": {},
                "Jack": {}
            },
            "Lily": {
                "Sophie": {}
            }
        },
        "Bob": {
            "Tom": {},
            "Lisa": {}
        }
    }
}

print("\nExtended family - Descendants of John:")
find_descendants("John", extended_family)