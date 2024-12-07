import unittest
from src.TextPreprocessingToolkit.tptk import TextPreprocessor
import pandas as pd


class TestFunctionalTextPreprocessor(unittest.TestCase):
    def setUp(self):
        self.text_preprocessor = TextPreprocessor()
        self.sample_dataset = pd.Series(
            [
                "I love programming!!!",
                "Isn't NLP amazing? Check: https://nlp.com",
                "<div>Remove this HTML</div>",
            ]
        )

    def test_preprocess_dataset(self):
        processed_dataset = self.sample_dataset.apply(self.text_preprocessor.preprocess)
        self.assertTrue(processed_dataset[0])
        self.assertNotIn("https://nlp.com", processed_dataset[1])
        self.assertNotIn("<div>", processed_dataset[2])


if __name__ == "__main__":
    unittest.main()
