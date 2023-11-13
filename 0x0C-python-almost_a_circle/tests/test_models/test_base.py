#!/usr/bin/python3


import unittest


class Test_Base(unittest.TestCase):
    def test_default_id_generation(self):
        obj1 = Base()
        obj2 = Base()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_custom_id(self):
        custom_id = 10
        obj = Base(id=custom_id)
        self.assertEqual(obj.id, custom_id)

    def test_id_increment(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)

    def test_id_initialization(self):
        initial_id = 5
        obj = Base(id=initial_id)
        self.assertEqual(obj.id, initial_id)

if __name__ == '__main__':
    unittest.main()
