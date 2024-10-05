# Tasks for Implementing a Binary Tree
# Task 1: Create the Node Class
# Create a class TreeNode with the following:

# A field data to store the node's value.
# A field left to store the reference to the left child node (initialize this to None).
# A field right to store the reference to the right child node (initialize this to None).
# # Implement a constructor (__init__) that initializes the data, left, and right fields.

# Task 2: Create the BinaryTree Class
# Create a class BinaryTree that contains the following:

# A field root to reference the root node of the tree (initialize to None).
# A method insert(data) to insert a new node into the tree (using BST rules).
# A method print_in_order() to print all elements in the tree in in-order traversal.


class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BSTree:
    root = None

    def insert(self,data):
        new_node = TreeNode(data)

        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while current:
                if data < current.next.data
                current = current.next
            current.next = new_node
