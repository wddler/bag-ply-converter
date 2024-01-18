import unittest
from bag_ply_converter import bag_to_ply
import os

class TestConvertion(unittest.TestCase):

    def test_convertion_ok(self):
        bag_to_ply("./test.bag")
        filename = "1.ply"
        result = os.path.isfile(filename)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
