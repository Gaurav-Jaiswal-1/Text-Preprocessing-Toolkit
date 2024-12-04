

# **Text Preprocessing Toolkit (TPTK)**

![Build Status](https://github.com/Gaurav-Jaiswal-1/Text-Preprocessing-Toolkit/actions/workflows/ci.yaml/badge.svg)  
_A comprehensive Python library to streamline text preprocessing tasks, designed for NLP projects._

---

## **Table of Contents**
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Getting Started](#getting-started)
    - [Basic Usage](#basic-usage)
    - [Custom Preprocessing](#custom-preprocessing)
5. [Examples](#examples)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)

---

## **Overview**

The **Text Preprocessing Toolkit (TPTK)** is a Python library designed to simplify the preprocessing of raw text data. Whether you're working on an NLP project, a machine learning pipeline, or simply cleaning text data, TPTK provides an easy-to-use, customizable solution for common text preprocessing needs.

---

## **Features**
- **Text Cleaning**:
  - Remove punctuation, special characters, HTML tags, and URLs.
- **Normalization**:
  - Convert text to lowercase, handle diacritics, and normalize Unicode.
- **Tokenization**:
  - Split text into words or sentences.
- **Stopword Removal**:
  - Remove common stopwords or use a custom list.
- **Lemmatization & Stemming**:
  - Normalize words to their base form.
- **Spell Correction**:
  - Automatically fix spelling errors.
- **Custom Pipelines**:
  - Select and order the preprocessing steps to suit your needs.

---

## **Installation**

Install the package using pip:

```bash
pip install TPTK
```

Alternatively, install directly from the GitHub repository:

```bash
pip install git+https://github.com/Gaurav-Jaiswal-1/Text-Preprocessing-Toolkit.git
```

---

## **Getting Started**

### **Basic Usage**
Import the library and start preprocessing:
```python
from TextPreprocessingToolkit.tptk import TextPreprocessor

# Initialize the preprocessor
preprocessor = TextPreprocessor()

# Sample text
text = "This is <b>sample</b> text with a URL: https://example.com and speelingg errors."

# Apply preprocessing
processed_text = preprocessor.preprocess(text)

print("Processed Text:", processed_text)
```

### **Custom Preprocessing**
You can define a custom pipeline for your preprocessing needs:
```python
custom_steps = [
    "lowercase",
    "remove_url",
    "remove_punctuation",
    "correct_spellings"
]

processed_text = preprocessor.preprocess(text, steps=custom_steps)
print("Custom Processed Text:", processed_text)
```

---

## **Examples**

### **Analyze Text Data**
You can pass a list of texts and get an overview of their structure:
```python
texts = [
    "Text example 1 with HTML tags <b>bold</b>!",
    "Another text with a URL: https://example.com.",
    "Missspelled word is heree!"
]

preprocessor.head(texts)
```

### **Preprocess a Dataset**
TPTK works seamlessly with pandas:
```python
import pandas as pd
from TextPreprocessingToolkit.tptk import TextPreprocessor

# Sample data
data = {"texts": ["Hello, <b>world</b>!", "Check out https://example.com.", "Thiss is a missspelled text."]}
df = pd.DataFrame(data)

# Initialize the preprocessor
preprocessor = TextPreprocessor()

# Apply preprocessing to a column
df["processed_texts"] = df["texts"].apply(preprocessor.preprocess)
print(df)
```

---

## **Contributing**

We welcome contributions to improve the toolkit! To contribute:
1. Fork the repository.
2. Clone your fork and create a new branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Make your changes and commit:
   ```bash
   git commit -m "Describe your changes"
   ```
4. Push your changes:
   ```bash
   git push origin feature-branch-name
   ```
5. Create a Pull Request (PR) to the main repository.

For detailed contribution guidelines, check the [CONTRIBUTING.md](CONTRIBUTING.md) file.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## **Contact**

For questions or support, feel free to reach out:
- **Author:** Gaurav Jaiswal
- **Email:** [jaiswalgaurav863@gmail.com](mailto:jaiswalgaurav863@gmail.com)
- **GitHub:** [@Gaurav-Jaiswal-1](https://github.com/Gaurav-Jaiswal-1)

