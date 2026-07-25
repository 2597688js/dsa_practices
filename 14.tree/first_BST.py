"""
Author : Janarddan Sarkar
File_name = first_bst.py
Date : 05-02-2024
Description :  ** Binary Tree ** is defined as a tree data structure where each node has at most 2 children.
Since each element in a binary tree can have only 2 children, we typically name them the left and right child.

** Binary Search Tree ** is a node-based binary tree data structure which has the following properties:
    1. The left subtree of a node contains only nodes with keys lesser than the node’s key.
    2. The right subtree of a node contains only nodes with keys greater than the node’s key.
    3. The left and right subtree each must also be a binary search tree.

We are going to implement Binary Search Tree here.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def append(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root

        if new_node.value == self.root.value:   # can not have two nodes with same value
            return False

        while temp is not None:
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right

    def contains(self, value):
        """
        checks if the given value exists in the BST
        """
        temp = self.root

        while temp is not None:
            if value < temp:
                temp = temp.left
            else:
                temp = temp.right


    def print_bst(self):
        """
        prints the BST from left to right starting from root.
        """
        temp = self.root

        while temp is not None:
            print(temp.value)
            temp = temp.left
            print(temp.value)


if __name__ == "__main__":
    bst1 = BinarySearchTree()
    bst1.append(10)
    bst1.append(5)
    bst1.append(18)
    bst1.append(15)
    bst1.append(9)

    print(bst1.root.value)
    print(bst1.root.left.value)
    print(bst1.root.left.right.value)
    print(bst1.root.right.value)
    print(bst1.root.right.left.value)




