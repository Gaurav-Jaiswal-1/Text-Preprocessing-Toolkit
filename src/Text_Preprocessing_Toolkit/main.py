# text_preprocessing_toolkit/preprocessing.py

import string
import re
import pandas as pd
from collections import Counter
from nltk.corpus import stopwords, wordnet
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag
from spellchecker import SpellChecker
import nltk
from IPython.display import display  # Importing the display function
import matplotlib.pyplot as plt

# Download required NLTK resources if not already downloaded
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')

class TextPreprocessor:
    def __init__(self):
        self.stopwords = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.spell = SpellChecker()
        self.ps = PorterStemmer()
        self.wordnet_map = {"N": wordnet.NOUN, "V": wordnet.VERB, "J": wordnet.ADJ, "R": wordnet.ADV}

    def remove_punctuation(self, text):
        if text:
            return text.translate(str.maketrans('', '', string.punctuation))
        return text

    def remove_stopwords(self, text):
        if text:
            return " ".join([word for word in text.split() if word not in self.stopwords])
        return text

    def remove_special_characters(self, text):
        if text:
            text = re.sub(r'[^a-zA-Z0-9]', ' ', text)
            text = re.sub(r'\s+', ' ', text)
            return text
        return text

    def stem_text(self, text):
        if text:
            return " ".join([self.ps.stem(word) for word in text.split()])
        return text

    def lemmatize_text(self, text):
        if text:
            pos_text = pos_tag(text.split())
            return " ".join([self.lemmatizer.lemmatize(word, self.wordnet_map.get(pos[0], wordnet.NOUN)) for word, pos in pos_text])
        return text

    def remove_url(self, text):
        if text:
            return re.sub(r'https?://\S+|www\.\S+', '', text)
        return text

    def remove_html_tags(self, text):
        if text:
            return re.sub(r'<[^>]+>', '', text)
        return text

    def correct_spellings(self, text):
        if text:
            corrected_text = []
            misspelled_words = self.spell.unknown(text.split())
            for word in text.split():
                if word in misspelled_words:
                    corrected_word = self.spell.correction(word)
                    corrected_text.append(corrected_word)
                else:
                    corrected_text.append(word)
            return " ".join(corrected_text)
        return text

    def lowercase(self, text):
        if text:
            return text.lower()
        return text

    def preprocess(self, text, steps=None):
        """
        Automatically preprocess text with a default pipeline. 
        User can specify steps for specific preprocessing order.
        
        Parameters:
        text (str): Text to preprocess.
        steps (list): List of preprocessing steps in desired order.

        Returns:
        str: Preprocessed text.
        """
        # Define the default pipeline
        default_pipeline = [
            "lowercase", "remove_punctuation", "remove_stopwords",
            "remove_special_characters", "remove_url", "remove_html_tags",
            "correct_spellings", "lemmatize_text"
        ]
        
        # Use steps if provided, otherwise default steps
        steps = steps if steps else default_pipeline
        for step in steps:
            text = getattr(self, step)(text)
        return text

    def head(self, texts, n=5):
        """
        Display a summary of the first few entries of the dataset for quick visualization.
        
        Parameters:
        texts (list or pd.Series): The dataset or list of text entries to display.
        n (int): The number of rows to display. Default is 5.
        
        Returns:
        None
        """
        if isinstance(texts, (list, pd.Series)):
            data = pd.DataFrame({"Text": texts[:n]})
            data['Word Count'] = data['Text'].apply(lambda x: len(x.split()))
            data['Character Count'] = data['Text'].apply(len)
            display(data)
            
        #     # Plotting word counts for quick overview
        #     plt.figure(figsize=(8, 5))
        #     plt.bar(range(n), data['Word Count'], color='skyblue')
        #     plt.xticks(range(n), [f'Text {i+1}' for i in range(n)], rotation=45)
        #     plt.xlabel('Text Entries')
        #     plt.ylabel('Word Count')
        #     plt.title('Word Count of First Few Text Entries')
        #     plt.show()
        # else:
        #     raise ValueError("The input should be a list or pandas Series of text entries.")
if __name__ == "__main__":
    TextPreprocessor()