# DoublyLinkedList.py
"""  """

class Node:
    """ Node class for DoublyLinkedList Class """
    def __init__(self, value, prev_node, next_node):
        self.value = value
        self.prev = prev_node
        self.next = next_node

class DoublyLinkedList:
    """ LinkedList class with knowledge of head and tail nodes """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
