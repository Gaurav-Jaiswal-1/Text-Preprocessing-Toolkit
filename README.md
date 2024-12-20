
# TextPreprocessor

A comprehensive and modular text preprocessing library for Natural Language Processing (NLP) tasks. It provides utilities for common preprocessing steps like tokenization, lemmatization, spell correction, and stopword removal, making it easier to prepare text data for machine learning and data analysis.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Preprocessing Steps](#preprocessing-steps)
- [Class Methods](#class-methods)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Customizable Pipeline**: Flexible pipeline to execute selected preprocessing steps.
- **Spell Correction**: Automatically fixes misspelled words.
- **Stopword Removal**: Supports customizable stopword lists.
- **Lemmatization**: Converts words to their base forms.
- **Punctuation and Special Character Removal**: Cleans the text by removing unnecessary characters.
- **URL and HTML Tag Removal**: Handles noisy inputs containing links and tags.
- **Dataset Preprocessing**: Processes datasets and provides statistics like word and character counts.
- **Logging**: Logs every preprocessing step for better debugging and transparency.

---

## Installation

To use the `TextPreprocessor` class, ensure you have Python 3.7+ installed. Clone this repository and install the required dependencies.

```bash
git clone https://github.com/your-username/TextPreprocessor.git
cd TextPreprocessor
pip install -r requirements.txt
```

---

## Usage

The `TextPreprocessor` class is designed to preprocess both individual text strings and datasets. Below is a quick example:

### Initializing the Preprocessor
```python
from text_preprocessor import TextPreprocessor

# Initialize with optional custom stopwords
preprocessor = TextPreprocessor(custom_stopwords=["example", "test"])
```

### Preprocessing Text
```python
sample_text = "This is an <b>example</b> text with a URL: https://example.com."
clean_text = preprocessor.preprocess(sample_text)
print(clean_text)
```

### Preprocessing a Dataset
```python
import pandas as pd

dataset = pd.Series([
    "This is an example text.",
    "HTML tags like <p> are removed.",
    "Misspelled wrods are corrected.",
    "12345 is just a number.",
    None
])

processed_data = preprocessor.preprocess_dataset(dataset)
print(processed_data)
```

---

## Preprocessing Steps

The `preprocess` function supports the following steps, which can be customized:
- `lowercase`: Converts text to lowercase.
- `remove_url`: Removes URLs from the text.
- `remove_html_tags`: Strips out HTML tags.
- `remove_punctuation`: Removes punctuation marks.
- `remove_special_characters`: Removes non-alphanumeric characters.
- `correct_spellings`: Corrects misspelled words.
- `lemmatize_text`: Lemmatizes words to their base forms.

Default steps can be modified by providing a `steps` parameter as a list when calling `preprocess`.

---

## Class Methods

- `tokenize(text: str) -> List[str]`: Tokenizes text into words.
- `remove_punctuation(text: str) -> str`: Removes punctuation.
- `remove_stopwords(tokens: List[str]) -> List[str]`: Removes stopwords from tokenized text.
- `remove_special_characters(text: str) -> str`: Removes special characters.
- `lemmatize_text(text: str) -> str`: Lemmatizes words using WordNet.
- `correct_spellings(text: str) -> str`: Corrects misspellings using `pyspellchecker`.
- `remove_url(text: str) -> str`: Removes URLs from text.
- `remove_html_tags(text: str) -> str`: Strips HTML tags from text.
- `preprocess(text: str, steps: Optional[List[str]] = None) -> str`: Preprocesses text based on selected steps.
- `preprocess_dataset(texts: Union[List[str], pd.Series], n: int = 5) -> pd.DataFrame`: Preprocesses a dataset of text entries.
- `head(text: str, n: int = 10) -> str`: Displays the first `n` characters of the text.

---

## Examples

### Custom Preprocessing
```python
text = "An EXAMPLE text with HTML <b>tags</b> and a URL: https://example.com."
custom_steps = ["lowercase", "remove_html_tags", "lemmatize_text"]
processed_text = preprocessor.preprocess(text, steps=custom_steps)
print(processed_text)
```

### Displaying Dataset Statistics
```python
dataset = pd.Series(["Sample text 1.", "Another <p>example</p>."])
preprocessor.preprocess_dataset(dataset)
```

### Using the `head` Function
```python
sample_text = "This is a sample text for the head function."
print(preprocessor.head(sample_text, 15))
```

---

## Contributing

We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a clear description of your changes.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- [NLTK](https://www.nltk.org) for NLP tools.
- [PySpellChecker](https://github.com/barrust/pyspellchecker) for spell checking.
- The Python community for inspiring open-source projects.
```

