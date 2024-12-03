import unittest
from src.Text_Preprocessing_Toolkit.TPT import TPT

class TestTPT(unittest.TestCase):
    def setUp(self):
        self.tpt = TPT()

    def test_remove_punctuation(self):
        text = "Hello, World!"
        result = self.tpt.remove_punctuation(text)
        self.assertEqual(result, "Hello World")

    def test_lowercase(self):
        text = "HeLLo"
        result = self.tpt.lowercase(text)
        self.assertEqual(result, "hello")

if __name__ == "__main__":
    unittest.main()
