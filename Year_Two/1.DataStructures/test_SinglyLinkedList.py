# ass3_TestSinglyLinkedList.py

import unittest
from SinglyLinkedList import Node
from SinglyLinkedList import SinglyLinkedList

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
    
    def test_nodeSetValueCorrect_success(self):
        self.node1.set_value(2)
        self.assertEqual(2, self.node1.get_value()) 

    def test_nodeSetValueNone_success(self):
        self.node1.set_value(None)
        self.assertEqual(1, self.node1.get_value()) 

    def test_nodeNextIsNone_success(self):
        self.assertIsNone(self.node1.get_next())
    
    def test_noneSetNext_success(self):
        self.node1.set_next(self.node2)
        self.assertEqual(self.node2, self.node1.get_next())
    
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

# pip install pytest
# Use pytest to test all cases beginning with test_ (even if main is not defined)

# pip install coverage
# coverage run ass3_SinglyLinkedList.py
# coverage report ass3_SinglyLinkedList.py
    # Name                       Stmts   Miss  Cover
    # ----------------------------------------------
    # ass3_SinglyLinkedList.py     102     65    36%
    # ----------------------------------------------
    # TOTAL                        102     65    36%
# coverage report -m ass3_SinglyLinkedList.py    
    # Name                       Stmts   Miss  Cover   Missing
    # --------------------------------------------------------
    # ass3_SinglyLinkedList.py     102     65    36%   20-22, 37, 44-51, 55-60, 64-73, 77-81, 85-95, 99-106, 110-125, 134
    # --------------------------------------------------------
    # TOTAL                        102     65    36%
# coverage html
    # generates htmlcov folder, view index.html to see clean report

# pip install pytest-cov
    # haven't figured out how to properly run this yet

if __name__ == "__main__":
    unittest.main()
