# SinglyLinkedList.py
""" contains Node class and SinglyLinkedList class """

class Node:
    """ simple Node class for Linked List Class """
    def __init__(self, value, prev_node, next_node):
        self.value = value
        self.prev = prev_node  # not used for singly linked list
        self.next = next_node

    def get_next(self):
        """ return the node after current node """
        return self.next

    def set_next(self, node):
        """ set the node to follow current node """
        self.next = node

    def get_value(self):
        """ return the value assigned to the current node """
        return self.value

    def set_value(self, value):
        """ set the value of the current node """
        if value is None:
            return
        self.value = value


class SinglyLinkedList:
    """ LinkedList class with only knowledge of head node """
    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        """ return the number of nodes in the LinkedList """
        return self.size

    def add_first(self, node):
        """ add node at the beginning of the list """
        if node is None:
            return
        node.set_next(self.head)
        self.head = node
        self.size += 1

    def add_last(self, node):
        """ add node at the end of the list """
        if self.size == 0:
            self.add_first(node)
        else:
            cur = self.head
            while cur.get_next() is not None:
                cur = cur.get_next()
            cur.set_next(node)
            self.size += 1

    def remove_first(self):
        """ remove the first node of the list """
        if self.size == 0:
            return
        old_head = self.head
        self.head = self.head.get_next()
        self.size -= 1
        old_head.set_next(None)

    def remove_last(self):
        """ remove the last node of the list """
        if self.size == 0:
            return
        if self.size == 1:
            self.remove_first()
        else:
            cur_node = self.head
            while cur_node.get_next().get_next() is not None:
                cur_node = cur_node.get_next()
            cur_node.set_next(None)
            self.size -= 1

    def add_after(self, new_node, existing_node):
        """ Insert new_node right after existing_node """
        if new_node is None or existing_node is None:
            return
        new_node.set_next(existing_node.get_next())
        existing_node.set_next(new_node)
        self.size += 1

    def add_before(self, new_node, existing_node):
        """ Insert new_node right before existing_node """
        if new_node is None or existing_node is None:
            return
        elif existing_node == self.head:
            self.add_first(new_node)
        else:
            cur_node = self.head
            while cur_node.get_next() != existing_node:
                cur_node = cur_node.get_next()
            new_node.set_next(existing_node)
            cur_node.set_next(new_node)
            self.size += 1

    def remove_after(self, target_node):
        """ remove the node that is right after target_node """
        if target_node is None:
            return
        if target_node.get_next() is None:
            return
        deleted_node = target_node.get_next()
        target_node.set_next(target_node.get_next().get_next())
        deleted_node.set_next(None)
        self.size -= 1

    def remove_before(self, target_node):
        """ remove the node that is right before target_node """
        if target_node is None:
            return
        if target_node == self.head:
            return
        if self.head.get_next() == target_node:
            old_head = self.head
            self.head = target_node
            old_head.set_next(None)
        else:
            cur_node = self.head
            while cur_node.get_next().get_next() != target_node:
                cur_node = cur_node.get_next()
            deleted_node = cur_node.get_next()
            cur_node.set_next(target_node)
            deleted_node.set_next(None)
        self.size -= 1

    def to_string(self):
        """ The concatenation of all the elements in the list """
        if self.size == 0:
            return "Linked List is empty"
        list_details = ""
        cur_node = self.head
        while cur_node.get_value() is not None:
            list_details = list_details + str(cur_node.get_value()) + " "
            if cur_node.next is not None:
                cur_node = cur_node.get_next()
            else:
                return list_details
