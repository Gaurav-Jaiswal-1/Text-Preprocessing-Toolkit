import pytest
from src.TextPreprocessingToolkit.tptk import TextPreprocessor

@pytest.fixture
def preprocessor():
    """Fixture to initialize the TextPreprocessor instance."""
    return TextPreprocessor()

def test_tokenize(preprocessor):
    text = "Hello, world!"
    tokens = preprocessor.tokenize(text)
    assert tokens == ["Hello", ",", "world", "!"], f"Unexpected result: {tokens}"

def test_remove_punctuation(preprocessor):
    text = "Hello, world!"
    processed_text = preprocessor.remove_punctuation(text)
    assert processed_text == "Hello world", f"Unexpected result: {processed_text}"

# Add additional tests for each function here
    