import unittest
from main import *


class TestTasks(unittest.TestCase):

    def test_is_sorted(self):
        false_result = is_sorted(ml_false)
        self.assertEqual(false_result, False)

        true_result = is_sorted(ml_true)
        self.assertEqual(true_result, True)
    

if __name__ == "__main__":
    unittest.main()
