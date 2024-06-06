import os
import pandas as pd
from pandas import read_csv
from joblib import dump, load
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from typing import Tuple, Optional

# Constants
ERROR_CREATING_MODEL = "Error creating model"

class EmailClassifier:
    """A classifier for emails based on their content."""

    def __init__(self, model_path: str, csv_file_path: str):
        """Initialize the classifier with the model and CSV file paths."""
        self.model_path = model_path
        self.csv_file_path = csv_file_path
        self.model, self.vectorizer = self.load_or_create_model()

    def load_data(self) -> Optional[pd.DataFrame]:
        """Load data from a CSV file."""
        try:
            df = read_csv(self.csv_file_path, encoding='utf-8')
            df['Message'].fillna('', inplace=True)  # replace np.nan values with an empty string
            return df
        except FileNotFoundError:
            raise
        except Exception as e:
            raise

    @staticmethod
    def train_model(messages: pd.Series, categories: pd.Series) -> Tuple[LogisticRegression, TfidfVectorizer]:
        """Train a model with the given messages and categories."""
        vectorizer = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
        messages_transformed = vectorizer.fit_transform(messages)
        model = LogisticRegression()
        model.fit(messages_transformed, categories)
        return model, vectorizer

    def create_model(self) -> Tuple[Optional[LogisticRegression], Optional[TfidfVectorizer]]:
        """Create a model from the data in the CSV file."""
        df = self.load_data()
        if df is not None:
            model, vectorizer = self.train_model(df['Message'], df['Category'])
            dump((model, vectorizer), self.model_path)
            return model, vectorizer
        raise Exception(ERROR_CREATING_MODEL)

    def load_model(self) -> Tuple[Optional[LogisticRegression], Optional[TfidfVectorizer]]:
        """Load a model from the model path."""
        if os.path.exists(self.model_path):
            try:
                model, vectorizer = load(self.model_path)
                return model, vectorizer
            except Exception as e:
                raise
        return None, None

    def load_or_create_model(self) -> Tuple[Optional[LogisticRegression], Optional[TfidfVectorizer]]:
        """Load a model, or create a new one if no model exists."""
        model, vectorizer = self.load_model()
        if model is None:
            model, vectorizer = self.create_model()
        return model, vectorizer

    def ensure_model(self):
        """Ensure that the model and vectorizer are loaded or created."""
        if self.model is None:
            self.model, self.vectorizer = self.create_model()
            if self.model is None:
                raise Exception(ERROR_CREATING_MODEL)

    def classify(self, text: str) -> str:
        """Classify a text as 'Ham mail' or 'Spam mail'."""
        self.ensure_model()
        input_data = self.vectorizer.transform([text])
        prediction = self.model.predict(input_data)
        return "Ham mail" if prediction[0] == 0 else "Spam mail"

    def calculate_accuracy(self) -> float:
        """Calculate the accuracy of the model."""
        df = self.load_data()
        if df is not None:
            # Split the data into a training set and a test set
            messages_train, messages_test, categories_train, categories_test = train_test_split(
                df['Message'], df['Category'], test_size=0.2, random_state=42)

            # Train the model on the training set
            model, vectorizer = self.train_model(messages_train, categories_train)

            # Use the model to make predictions on the test set
            messages_test_transformed = vectorizer.transform(messages_test)
            predictions = model.predict(messages_test_transformed)

            # Calculate the accuracy of the model
            accuracy = accuracy_score(categories_test, predictions)
            return accuracy

        raise Exception(ERROR_CREATING_MODEL)


