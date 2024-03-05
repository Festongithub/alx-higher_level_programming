#!/usr/bin/python3
import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):

    def test_id_incrementation(self):
        # Test that the id is incremented correctly
        obj1 = Base()
        obj2 = Base()

        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_custom_id(self):
        # Test that custom id is assigned when provided
        obj3 = Base(id=100)

        self.assertEqual(obj3.id, 100)

    def test_no_id_argument(self):
        # Test that id is automatically assigned when no id is provided
        obj4 = Base()
        obj5 = Base()

        self.assertEqual(obj4.id, 3)  # 1 (from previous tests) + 2 (new instances)
        self.assertEqual(obj5.id, 4)

if __name__ == '__main__':
    unittest.main()
