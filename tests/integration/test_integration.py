import unittest
from TextPreprocessingToolkit import TextPreprocessor


class TestTextPreprocessorIntegration(unittest.TestCase):
    def setUp(self):
        self.text_preprocessor = TextPreprocessor()
        self.sample_texts = [
            "Hello, World! Visit https://example.com for more info.",
            "<h1>Title</h1><p>This is a paragraph.</p>",
            "Speling erors are comman in texts.",
        ]

    def test_full_pipeline(self):
        expected_results = [
            "hello world visit example com for more info",
            "title this is a paragraph",
            "spelling errors are common in texts",
        ]
        for text, expected in zip(self.sample_texts, expected_results):
            result = self.text_preprocessor.preprocess(text)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
