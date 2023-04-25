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
        self.node4 = Node(4, None, None)

    def test_creationOfInstances_success(self):
        self.assertIsNotNone(self.my_linked_list)
        self.assertIsNotNone(self.node1)

    def test_nodeGetValue_success(self):
        self.assertEqual(1, self.node1.get_value())            
    
    def test_nodeNextIsNone_success(self):
        self.assertIsNone(self.node1.get_next())
    
    def test_linkedListEmpty_success(self):
        self.assertIsNone(self.my_linked_list.head)

    def test_addFirst_success(self):
        self.my_linked_list.add_first(self.node1)
        self.assertEqual("1 ", self.my_linked_list.to_string())
        self.assertNotEqual("1", self.my_linked_list.to_string())
        self.assertNotEqual("2", self.my_linked_list.to_string())

    def test_linkedListSize_success(self):
        self.assertEqual(0, self.my_linked_list.get_size())
        self.my_linked_list.add_first(self.node1)
        self.assertNotEqual(0, self.my_linked_list.get_size())
        self.assertEqual(1, self.my_linked_list.get_size())
        self.my_linked_list.add_first(self.node2)
        self.assertNotEqual(1, self.my_linked_list.get_size())
        self.assertEqual(2, self.my_linked_list.get_size())



if __name__ == "__main__":
    unittest.main()