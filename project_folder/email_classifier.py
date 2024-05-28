import os
from pandas import read_csv
from joblib import dump, load
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


class EmailClassifier:
    def __init__(self, model_path: str, csv_file_path: str):
        self.model_path = model_path
        self.csv_file_path = csv_file_path
        self.model = self.load_model()
        if self.model is None:
            print("Model is not loaded. Creating model soon...")
            self.create_model()

    def load_data(self):
        try:
            return read_csv(self.csv_file_path, encoding='utf-8')
        except FileNotFoundError:
            print("Error: CSV file not found")
        except Exception as e:
            print(f"Error: An unexpected error occurred - {str(e)}")

    @staticmethod
    def train_model(messages, categories):
        vectorizer = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
        messages_transformed = vectorizer.fit_transform(messages)

        model = LogisticRegression()
        model.fit(messages_transformed, categories)

        return model, vectorizer

    def create_model(self):
        if not os.path.exists(self.model_path):
            df = self.load_data()
            if df is not None:
                dump(self.train_model(df['Message'], df['Category']), self.model_path)
                return "Model created successfully"
            else:
                return "Error loading data"
        else:
            return "Model already exists"

    def load_model(self):
        if not os.path.exists(self.model_path):
            print("Model file does not exist. A new model will be created when needed.")
            return None
        return load(self.model_path)

    def classify(self, text: str) -> str:
        input_data, prediction = self.model[1].transform([text]), self.model[0].predict(self.model[1].transform([text]))
        return "Ham mail" if prediction[0] == 0 else "Spam mail"
