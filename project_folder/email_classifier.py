import os
import pandas as pd
from joblib import dump, load
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

csv_file_path = r"/Users/aidaz/PycharmProjects/Project/Chrome_Extensions_Spam_Mail/project_folder/final.csv"


def load_data(csv_file_path):
    try:
        return pd.read_csv(csv_file_path, encoding='utf-8')
    except FileNotFoundError:
        print("Error: CSV file not found")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {str(e)}")


def preprocess_data(df):
    df = df.fillna('')  # Replace NaN with empty string
    return df['Message'], df['Category']


def train_model(messages, categories):
    vectorizer = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
    messages_transformed = vectorizer.fit_transform(messages)

    model = LogisticRegression()
    model.fit(messages_transformed, categories)

    return model, vectorizer

def classify_email(input_mail, model):
    input_data = model[1].transform([input_mail])
    prediction = model[0].predict(input_data)
    return "Ham mail" if prediction[0] == 0 else "Spam mail"


def create_model(csv_file_path):
    if not os.path.exists('model.joblib'):
        df = load_data(csv_file_path)
        if df is not None:
            messages, categories = preprocess_data(df)
            dump(train_model(messages, categories), 'model.joblib')
        else:
            print("Error loading data")
    else:
        print("Model already exists")
    return dump('model.joblib')


def just_create_model():
    model = create_model(csv_file_path)
    print("Model created successfully" if model else "Error creating model")


def main():
    just_create_model()


if __name__ == "__main__":
    main()
