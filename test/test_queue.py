import unittest


class TestFunctions(unittest.TestCase):
    def test_requestor(self):
        ans1 = 1
        ans2 = 1

        self.assertEqual(ans1, ans2)

if __name__ == "__main__":
    unittest.main()