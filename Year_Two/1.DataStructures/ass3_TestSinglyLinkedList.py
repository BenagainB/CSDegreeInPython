# ass3_TestSinglyLinkedList.py

import unittest
from ass3_SinglyLinkedList import Node
from ass3_SinglyLinkedList import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):
    def setUp(self):
        self.my_linked_list = SinglyLinkedList()
        self.node1 = Node(1, None, None)
        self.node2 = Node(2, None, None)
        self.node3 = Node(3, None, None)
        print("Hello")

    def test_get_next_success(self):







if __name__ == "__main__":
    unittest.main()