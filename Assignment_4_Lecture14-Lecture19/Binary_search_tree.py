'''
10. Binary Search Tree (Classes + Recursion)
Task: Implement a BST with recursive insert/search/traversal.
Input:
bst = BinarySearchTree()
for num in [7, 3, 9, 1, 5]:
bst.insert(num)
bst.inorder_traversal()
Expected Output:
[1, 3, 5, 7, 9]
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)
        if value < node.data:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        return node

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        if value == node.data:
            return True
        elif value < node.data:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def inorder_traversal(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.left) + [node.data] + self._inorder(node.right)

bst = BinarySearchTree()
for num in [7, 3, 9, 1, 5]:
    bst.insert(num)
print(bst.inorder_traversal())  