class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)

        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    def search(self, root, data):
        if root is None:
            return False

        if root.data == data:
            return True

        if data < root.data:
            return self.search(root.left, data)

        return self.search(root.right, data)

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


bst = BinarySearchTree()

numbers = [50, 30, 70, 20, 40, 60, 80]

for number in numbers:
    bst.root = bst.insert(bst.root, number)

print("Inorder Traversal:", end=" ")
bst.inorder(bst.root)

print()

value = int(input("Enter element to search: "))

if bst.search(bst.root, value):
    print("Element found in BST.")
else:
    print("Element not found in BST.")
