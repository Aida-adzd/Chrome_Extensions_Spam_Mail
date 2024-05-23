import numpy as np
import os
import pandas as pd
from joblib import dump, load
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
def load_data(csv_file_path):
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            df = pd.read_csv(file)
        return df
    except FileNotFoundError:
        print("Error: CSV file not found")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred - {str(e)}")
        return None

def preprocess_data(df):
    # Data cleaning and transformation
    mail_data = df.fillna('')  # Replace NaN with empty string
    mail_data['Category'] = mail_data['Category'].apply({'ham': 0, 'spam': 1}.get)
    
    # Split data into input (X) and output (Y)
    X = mail_data['Message']
    Y = mail_data['Category']
    
    return X, Y

def train_model(X_train, Y_train):
    # Check if model is already trained
    if os.path.exists('model.joblib'):
        lrm, feature_extraction = load('model.joblib')
    else:
        # Feature extraction using TF-IDF
        feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
        x_train_feature = feature_extraction.fit_transform(X_train)

        # Train the model
        lrm = LogisticRegression()
        lrm.fit(x_train_feature, Y_train)

        # Save the model
        dump((lrm, feature_extraction), 'model.joblib')

    return lrm, feature_extraction
def evaluate_model(model, X_test, Y_test):
    # Use the model for predictions
    x_test_feature = model[1].transform(X_test)
    prediction_test = model[0].predict(x_test_feature)
    
    # Evaluate model performance
    test_accuracy = accuracy_score(Y_test, prediction_test)
    conf_matrix = confusion_matrix(Y_test, prediction_test)
    class_report = classification_report(Y_test, prediction_test)
    
    return test_accuracy, conf_matrix, class_report

def classify_email(input_mail, model):
    # Predict for the input email
    input_data = model[1].transform([input_mail])  # Note: Passing a list with one element
    prediction = model[0].predict(input_data)
    
    if prediction[0] == 0:
        return "Ham mail"
    else:
        return "Spam mail"

def get_text(text):
    csv_file_path = r"D:\Amir\Uni\osoltarahi_narmafzar\project\Chrome_Extensions_Spam_Mail\project_folder\mail_data.csv"
    df = load_data(csv_file_path)
    if df is not None:
        X, Y = preprocess_data(df)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)
        model = train_model(X_train, Y_train)
        test_accuracy, conf_matrix, class_report = evaluate_model(model , X_test , Y_test)
        result = classify_email(text, model)
        return result

def  main():
    text = input("text:")
    result = get_text(text)
    print(result)
    
if __name__ == "__main__":
    main()
    
    
    
