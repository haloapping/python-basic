import unittest


class TestStringMethods(unittest.TestCase):
    def test_strip(self):
        self.assertEqual("rahelcuek".strip("ek"), "rahelcu")

    def test_isalnum(self):
        self.assertTrue('appi223ng'.isalnum())
        self.assertFalse('__'.isalnum())

    def test_index(self):
        string = "Rahel"
        self.assertEqual(string.index("hel"), 2)

        with self.assertRaises(ValueError):
            string.index("Hi")


if __name__ == "__main__":
    unittest.main()
