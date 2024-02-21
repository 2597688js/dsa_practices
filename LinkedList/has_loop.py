"""
Author : Janarddan Sarkar
File_name = has_loop.py
Date : 23-01-2024
Description :  Write a method called has_loop that is part of the linked list class.

The method should be able to detect if there is a cycle or loop present in the linked list.

     head -> 11 ➡️ 3
             ⬆️    ⬇️
      tail -> 7 ⬅️ 23️

Logic :
1. Create two pointers, slow and fast, both initially pointing to the head of the linked list.

2. Traverse the list with the slow pointer moving one step at a time, while the fast pointer moves two steps at a time.

3. If there is a loop in the list, the fast pointer will eventually meet the slow pointer. If this occurs, the method
should return True.

4. If the fast pointer reaches the end of the list or encounters a None value, it means there is no loop in the list.
 In this case, the method should return False.

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def has_loop(self):
        slow, fast = self.head, self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop())  # Returns True

my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop())  # Returns False

"""
    EXPECTED OUTPUT:
    ----------------
    True
    False

"""
