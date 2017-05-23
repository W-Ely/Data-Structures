"""This module creates a linked list data structure."""


class Node(object):

    def __init__(self, value=None, next_node=None):
        """Initalizes a node."""
        self.value = value
        self.next_node = next_node


class LinkedList(object):

    def __init__(self, head=None, tail=None):
        """Initalizes a linked list"""
        self.head = head
        # self.tail = head

    def push(self, val):
        new_node = Node(val, self.head)
        self.head = new_node

    def pop(self):
        try:
            val = self.head.value
            self.head = self.head.next_node
            return val
        except AttributeError:
            print("Can not pop from empty list.")
            return "Can not pop from empty list."

    def size(self):
        count = 0
        head = self.head
        while head is not None:
            count += 1
            head = head.next_node
        return count

    def search(self, val):
        check = self.head
        while check.value is not None:
            print(check.value)
            if check.value == val:
                return check
            else:
                check = self.head.next_node
        return None

    def remove(self, node):
        check = self.head
        if check == node:
            self.pop()
            return
        while check.next_node is not node and check.next_node is not None:
            check = check.next_node
        if check.next_node is None:
            raise AttributeError("Can not remove node, not found.")
        else:
            check.next_node = check.next_node.next_node


# a_node = Node('testing')
a_linked_list = LinkedList()
# print(a_linked_list.head)
a_linked_list.push(5)
a_linked_list.push(15)
print(a_linked_list.search("nope"))
