# tests/test_preprocessing_integration.py

import pytest
from text_preprocessing_toolkit.preprocessing import TextPreprocessor

processor = TextPreprocessor()

def test_preprocess_pipeline():
    text = "HELLO, this is a Sample text with URL https://example.com and HTML <p>tags</p>."
    expected = "hello sample text url tags"  # Expected outcome after all processing steps
    processed_text = processor.preprocess(
        text, 
        steps=[
            "lowercase", "remove_punctuation", "remove_stopwords",
            "remove_special_characters", "remove_url", "remove_html_tags",
            "correct_spellings", "lemmatize_text"
        ]
    )
    assert processed_text == expected

# Test with different text cases to check end-to-end processing
