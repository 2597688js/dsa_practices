"""
Author : Janarddan Sarkar
File_name = ll1.py
Date : 08-01-2024
Description :  
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LL: # Linked List
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.next = None

    # insert at the beginning
    def prepend(self, value):
        new_node = Node(value)
        # if the linked list is empty
        if self.head is None:
            self.head = new_node
            self.next = new_node
            return
        # if the linked list is not empty
        else:
            new_node.next = self.head
            self.head = new_node
            self.next = new_node

    # insert at the end
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.next = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    # print the linked list
    def print_ll(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=' -> ')
            current_node = current_node.next


if __name__ == "__main__":
    my_ll = LL(2)
    # my_ll.print_ll()
    my_ll.prepend(1)
    # my_ll.print_ll()
    my_ll.append(3)
    my_ll.print_ll()
