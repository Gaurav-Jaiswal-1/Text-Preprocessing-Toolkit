import pytest
from src.TextPreprocessingToolkit.tptk import TextPreprocessor

@pytest.fixture
def preprocessor():
    """Fixture to initialize the TextPreprocessor instance."""
    return TextPreprocessor()

def test_preprocess_pipeline(preprocessor):
    text = "Running wolves are quickly eating. Visit https://example.com for details!"
    steps = [
        "lowercase",
        "remove_punctuation",
        "remove_stopwords",
        "remove_special_characters",
        "remove_url",
        "lemmatize_text",
    ]
    processed_text = preprocessor.preprocess(text, steps=steps)
    expected = "run wolf quickly eat visit detail"
    assert processed_text == expected, f"Unexpected result: {processed_text}"
