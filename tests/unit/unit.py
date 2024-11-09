# tests/test_preprocessing_unit.py

import pytest
from text_preprocessing_toolkit.preprocessing import TextPreprocessor

processor = TextPreprocessor()

def test_remove_punctuation():
    text = "Hello, world!"
    expected = "Hello world"
    assert processor.remove_punctuation(text) == expected

def test_remove_stopwords():
    text = "This is a sample text"
    expected = "sample text"  # assuming 'this', 'is', 'a' are stopwords
    assert processor.remove_stopwords(text) == expected

def test_lowercase():
    text = "HELLO"
    expected = "hello"
    assert processor.lowercase(text) == expected

# Add more tests for each method with various edge cases
