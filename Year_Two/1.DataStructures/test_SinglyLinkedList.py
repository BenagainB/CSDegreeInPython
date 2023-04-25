# test_SinglyLinkedList.py
""" test cases for SinglyLinkedList """

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
        self.node5 = Node(5, None, None)

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
        self.assertEqual(None, self.my_linked_list.add_first(None))

    def test_addLast_success(self):
        self.my_linked_list.add_last(self.node1)
        self.assertEqual("1 ", self.my_linked_list.to_string())
        self.assertNotEqual("1", self.my_linked_list.to_string())
        self.assertNotEqual("2", self.my_linked_list.to_string())
        self.assertEqual(None, self.my_linked_list.add_first(None))
        self.my_linked_list.add_last(self.node2)
        self.assertNotEqual("2", self.my_linked_list.to_string())
        self.assertEqual("1 2 ", self.my_linked_list.to_string())
        self.my_linked_list.add_last(self.node3)
        self.assertNotEqual("1 2 ", self.my_linked_list.to_string())
        self.assertEqual("1 2 3 ", self.my_linked_list.to_string())

    def test_removeFirst_success(self):
        self.my_linked_list.add_first(self.node1)
        self.my_linked_list.add_last(self.node2)
        self.assertEqual("1 2 ", self.my_linked_list.to_string())
        self.my_linked_list.remove_first()
        self.assertEqual("2 ", self.my_linked_list.to_string())
        self.my_linked_list.remove_first()
        self.assertEqual("Linked List is empty", self.my_linked_list.to_string())
        self.my_linked_list.remove_first()
        self.assertEqual("Linked List is empty", self.my_linked_list.to_string())

    def test_removeLast_success(self):
        self.my_linked_list.add_first(self.node1)
        self.my_linked_list.add_last(self.node2)
        self.my_linked_list.add_last(self.node3)
        self.assertEqual("1 2 3 ", self.my_linked_list.to_string())
        self.my_linked_list.remove_last()
        self.assertEqual("1 2 ", self.my_linked_list.to_string())
        self.my_linked_list.remove_last()
        self.assertEqual("1 ", self.my_linked_list.to_string())
        self.my_linked_list.remove_last()
        self.assertEqual("Linked List is empty", self.my_linked_list.to_string())
        self.my_linked_list.remove_last()
        self.assertEqual("Linked List is empty", self.my_linked_list.to_string())

    def test_addAfter_success(self):
        self.assertEqual("Linked List is empty", self.my_linked_list.to_string())
        self.my_linked_list.add_after(None, None)
        self.assertEqual("Linked List is empty", self.my_linked_list.to_string())
        self.my_linked_list.add_after(self.node1, None)
        self.assertEqual("Linked List is empty", self.my_linked_list.to_string())
        self.my_linked_list.add_after(None, self.node1)
        self.assertEqual("Linked List is empty", self.my_linked_list.to_string())
        self.my_linked_list.add_first(self.node1)
        self.my_linked_list.add_after(None, self.node1)
        self.assertEqual("1 ", self.my_linked_list.to_string())
        self.my_linked_list.add_after(self.node2, self.node1)
        self.assertEqual("1 2 ", self.my_linked_list.to_string())

    def test_addBefore_success(self):
        self.assertEqual("Linked List is empty", self.my_linked_list.to_string())
        self.my_linked_list.add_before(None, None)
        self.assertEqual("Linked List is empty", self.my_linked_list.to_string())
        self.my_linked_list.add_before(self.node1, None)
        self.assertEqual("Linked List is empty", self.my_linked_list.to_string())
        self.my_linked_list.add_before(None, self.node1)
        self.assertEqual("Linked List is empty", self.my_linked_list.to_string())
        self.my_linked_list.add_first(self.node5)
        self.assertEqual("5 ", self.my_linked_list.to_string())
        self.my_linked_list.add_before(None, self.node5)
        self.assertEqual("5 ", self.my_linked_list.to_string())
        self.my_linked_list.add_before(self.node3, self.node5)
        self.assertEqual("3 5 ", self.my_linked_list.to_string())
        self.my_linked_list.add_before(self.node1, self.node3)
        self.assertEqual("1 3 5 ", self.my_linked_list.to_string())
        self.my_linked_list.add_before(self.node2, self.node3)
        self.assertEqual("1 2 3 5 ", self.my_linked_list.to_string())
        self.my_linked_list.add_before(self.node4, self.node5)
        self.assertEqual("1 2 3 4 5 ", self.my_linked_list.to_string())

    def test_removeAfter_success(self):
        self.assertEqual("Linked List is empty", self.my_linked_list.to_string())
        self.my_linked_list.add_first(self.node1)
        self.my_linked_list.add_last(self.node2)
        self.assertEqual("1 2 ", self.my_linked_list.to_string())
        self.my_linked_list.remove_after(None)
        self.assertEqual("1 2 ", self.my_linked_list.to_string())
        self.my_linked_list.remove_after(self.node2)
        self.assertEqual("1 2 ", self.my_linked_list.to_string())
        self.my_linked_list.remove_after(self.node1)
        self.assertEqual("1 ", self.my_linked_list.to_string())

    def test_removeBefore_success(self):
        self.assertEqual("Linked List is empty", self.my_linked_list.to_string())
        self.my_linked_list.add_first(self.node1)
        self.my_linked_list.add_last(self.node2)
        self.my_linked_list.add_last(self.node3)
        self.my_linked_list.add_last(self.node4)
        self.my_linked_list.add_last(self.node5)
        self.assertEqual("1 2 3 4 5 ", self.my_linked_list.to_string())
        self.my_linked_list.remove_before(None)
        self.assertEqual("1 2 3 4 5 ", self.my_linked_list.to_string())
        self.my_linked_list.remove_before(self.node1)
        self.assertEqual("1 2 3 4 5 ", self.my_linked_list.to_string())
        self.my_linked_list.remove_before(self.node2)
        self.assertEqual("2 3 4 5 ", self.my_linked_list.to_string())
        self.my_linked_list.remove_before(self.node5)
        self.assertEqual("2 3 5 ", self.my_linked_list.to_string())

    def test_linkedListSize_success(self):
        self.assertEqual(0, self.my_linked_list.get_size())
        self.my_linked_list.add_first(self.node1)
        self.assertNotEqual(0, self.my_linked_list.get_size())
        self.assertEqual(1, self.my_linked_list.get_size())
        self.my_linked_list.add_first(self.node2)
        self.assertNotEqual(1, self.my_linked_list.get_size())
        self.assertEqual(2, self.my_linked_list.get_size())

# python test_SinglyLinkedList.py
    # ...........
    # ----------------------------------------------------------------------
    # Ran 16 tests in 0.000s
    # OK

# pip install pytest
# Use pytest to test all cases beginning with test_ (even if main is not defined)

# pip install coverage
# coverage run SinglyLinkedList.py
# coverage report ass3_SinglyLinkedList.py
    # Name                  Stmts   Miss  Cover
    # -----------------------------------------
    # SinglyLinkedList.py     105      0   100%
    # -----------------------------------------
    # TOTAL                   105      0   100%
# coverage report -m SinglyLinkedList.py
    # Name                  Stmts   Miss  Cover   Missing
    # ---------------------------------------------------
    # SinglyLinkedList.py     105      0   100%
    # ---------------------------------------------------
    # TOTAL                   105      0   100%
# coverage html
    # generates htmlcov folder, view index.html to see clean report

# pip install pytest-cov
# pytest --cov=SinglyLinkedList
    # collected 16 items
    # test_SinglyLinkedList.py .........                                                    [100%]
    # ---------- coverage: platform darwin, python 2.7.18-final-0 ----------
    # Name                  Stmts   Miss  Cover
    # -----------------------------------------
    # SinglyLinkedList.py     105      0   100%
    # -----------------------------------------
    # TOTAL                   105      0   100%
    # ========== 16 passed in 0.11 seconds ======================================================

if __name__ == "__main__":
    unittest.main()
