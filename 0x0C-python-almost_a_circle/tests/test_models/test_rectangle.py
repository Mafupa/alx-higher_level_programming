import unittest

class TestRectangleClass(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(width=4, height=3, x=1, y=2, id=1)

    def test_attributes(self):
        self.assertEqual(self.rectangle.width, 4)
        self.assertEqual(self.rectangle.height, 3)
        self.assertEqual(self.rectangle.x, 1)
        self.assertEqual(self.rectangle.y, 2)
        self.assertEqual(self.rectangle.id, 1)

    def test_width_validation(self):
        with self.assertRaises(TypeError):
            self.rectangle.width = "invalid"
        with self.assertRaises(ValueError):
            self.rectangle.width = 0

    def test_height_validation(self):
        with self.assertRaises(TypeError):
            self.rectangle.height = "invalid"
        with self.assertRaises(ValueError):
            self.rectangle.height = 0

    def test_area_calculation(self):
        self.assertEqual(self.rectangle.area(), 4 * 3)

    def test_display_method(self):
        expected_output = "\n\n   ####\n   ####\n   ####\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.rectangle.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str_method(self):
        expected_str = "[Rectangle] (1) 1/2 - 4/3"
        self.assertEqual(str(self.rectangle), expected_str)

if __name__ == '__main__':
    unittest.main()

