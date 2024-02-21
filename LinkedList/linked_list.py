"""
Author : Janarddan Sarkar
File_name = linked_list.py
Date : 17-01-2024
Description :  All the Singly Linked List Methods
"""


class Node:
    """
    Creates a Node
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        """
        creates new Node
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        """
        create new Node
        add Node to the end
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop_first(self):
        """
        removes the first node from the linked list and returns the node
        """
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None

            self.length -= 1
            # if the LL contains only 1 node
            if self.length == 0:
                self.tail = None
            return temp

    def pop(self):
        """
        removes the node from the end and return it
        """
        if self.head is None:  # if LL is empty
            return None
        else:
            pre = self.head
            temp = self.head
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None

            self.length -= 1
            # if there is only 1 node in the LL
            if self.length == 0:
                self.head = None
                self.tail = None

            return temp.value

    def prepend(self, value):
        """
        create new Node
        add Node to the beginning
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def get_node(self, index):
        """
        Get the node at given index
        """
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def set_node_value(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:   # set the value of head node
            self.head.value = value
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.value = value

    def insert(self, index, value):
        """
        create new Node
        insert Node to the given index
        """

        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(value)
        if index == self.length:
            self.append(value)

        new_node = Node(value)
        temp = self.head
        for _ in range(index-1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

    def remove(self, index):
        """
        remove the node from the given index.
        case1 : remove the first node (head has to be shifted to the next node)-> pop_first
        case2 : remove the last node (tail has to be shifted to the previous node)-> pop
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.pop_first()
        if index == self.length - 1:
            self.pop()

        prev_node = self.get_node(index-1)
        curr_node = prev_node.next

        prev_node.next = curr_node.next
        curr_node.next = None

        self.length -= 1

        return curr_node

    def reverse(self):
        """
        reverses the linked list
        """
        temp = self.head
        self.head = self.tail
        self.tail = temp    # upto here we're basically swapping head and tail

        # after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def print_list(self):
        """
        prints the linked list values
        """
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end='->')
            current_node = current_node.next


if __name__ == "__main__":
    # my_ll = LinkedList(4)
    # print(my_ll.head.value)

    # --- append ----
    # my_ll = LinkedList(1)
    # my_ll.append(2)

    # ---- pop ------
    # (2) Items
    # print(my_ll.pop())
    # # (1) Item
    # print(my_ll.pop())
    # # (0) Item
    # print(my_ll.pop())

    # --- prepend ------
    # my_ll.prepend(4)
    # my_ll.print_list()

    # --- pop first ----
    # 2 Items
    # print(my_ll.pop_first())
    # # 1 Item
    # print(my_ll.pop_first())
    # # 0 Item
    # print(my_ll.pop_first())

    # -- get ------
    # my_ll = LinkedList(0)
    # my_ll.append(1)
    # my_ll.append(2)
    # my_ll.append(3)
    #
    # print(my_ll.get(3))
    # print(my_ll.get(2))

    # ---- set node value ----
    ll = LinkedList(1)
    ll.append(1)
    ll.append(3)
    ll.append(4)

    ll.print_list()
    print("\nafter set node value ")
    ll.set_node_value(3, 33)
    ll.print_list()

    # ----- insert ------
    # ll1 = LinkedList(1)
    # ll1.append(2)
    # ll1.append(3)
    # ll1.append(5)
    #
    # ll1.insert(3, 4)
    # ll1.insert(5, 99)
    #
    # ll1.print_list()

    # ----- remove ----
    # ll1 = LinkedList(1)
    # ll1.append(2)
    # ll1.append(3)
    # ll1.append(5)
    #
    # ll1.print_list()
    #
    # print(ll1.remove(1))
    # print(" After removal ")
    # ll1.print_list()

    # ---- reverse ------
    # ll1 = LinkedList(1)
    # ll1.append(2)
    # ll1.append(3)
    # ll1.append(4)
    #
    # ll1.print_list()
    # print("\nAfter reversing ")
    # ll1.reverse()
    # ll1.print_list()

