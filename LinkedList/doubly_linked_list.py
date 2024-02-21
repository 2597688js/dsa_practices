"""
Author : Janarddan Sarkar
File_name = doubly_linked_list.py
Date : 31-01-2024
Description :  
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        """
        add node at the end of the linked list
        """
        new_node = Node(value)
        # If there is no node
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        # If there is no node
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

    def pop_first(self):
        """
        return: removes the first node from the linked list and return it
        """
        if self.head is None:
            return None

        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None

            self.length -= 1

            return temp
        else:
            self.head.prev = None
            self.head = self.head.next
            temp.next = None

            self.length -= 1

            return temp

    def print_list(self):
        """
        prints the doubly linked list
        """
        temp = self.head
        while temp is not None:
            print(temp.value, end=' <-> ')
            temp = temp.next


if __name__ == "__main__":
    dll = DoublyLinkedList(2)
    dll.append(3)
    # dll.prepend(1)

    # dll.print_list()
    print(dll.pop_first())
    print(dll.pop_first())
    print(dll.pop_first())


