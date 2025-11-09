import unittest
from DataPreprocessingToolkit.text_preprocessor import TextPreprocessor


class TestTextPreprocessor(unittest.TestCase):
    def setUp(self):
        # Initialize the TextPreprocessor instance
        self.text_preprocessor = TextPreprocessor()
        self.sample_text = "This is an Example Text, with Punctuations! And some URLs: https://example.com"
        self.tokenized_text = ["This", "is", "an", "Example", "Text", "with", "Punctuations", "And", "some", "URLs"]

    def test_tokenize(self):
        tokens = self.text_preprocessor.tokenize(self.sample_text)
        self.assertEqual(tokens, self.tokenized_text)

    def test_lowercase(self):
        result = self.text_preprocessor.lowercase(self.sample_text)
        self.assertEqual(result, self.sample_text.lower())

    def test_remove_punctuation(self):
        result = self.text_preprocessor.remove_punctuation(self.sample_text)
        self.assertEqual(result, "This is an Example Text with Punctuations And some URLs httpexamplecom")

    def test_remove_special_characters(self):
        result = self.text_preprocessor.remove_special_characters(self.sample_text)
        self.assertEqual(result, "This is an Example Text with Punctuations And some URLs https://example.com")

    def test_remove_stopwords(self):
        tokens = self.text_preprocessor.tokenize(self.sample_text)
        result = self.text_preprocessor.remove_stopwords(tokens)
        expected = ["Example", "Text", "Punctuations", "URLs"]
        self.assertEqual(result, expected)

    def test_correct_spellings(self):
        text = "Ths is an exmple of txt with speling erors"
        result = self.text_preprocessor.correct_spellings(text)
        self.assertEqual(result, "This is an example of text with spelling errors")

    def test_lemmatize_text(self):
        text = "The cats are running"
        result = self.text_preprocessor.lemmatize_text(text)
        self.assertEqual(result, "The cat be run")

    def test_preprocess_pipeline(self):
        result = self.text_preprocessor.preprocess(self.sample_text)
        self.assertIsInstance(result, str)
        self.assertTrue(result)

    def test_remove_url(self):
        result = self.text_preprocessor.remove_url(self.sample_text)
        self.assertNotIn("https://example.com", result)

    def test_remove_html_tags(self):
        html_text = "<p>This is a paragraph.</p><a href='example.com'>Link</a>"
        result = self.text_preprocessor.remove_html_tags(html_text)
        self.assertEqual(result, "This is a paragraph.Link")


if __name__ == "__main__":
    unittest.main()
