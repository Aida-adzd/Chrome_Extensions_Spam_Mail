from joblib import load
import os
from email_classifier import just_create_model
def load_model():
    if 'model.joblib' not in os.listdir():
        just_create_model()
    return load('model.joblib')

def classify_text(text):
    model = load_model()
    input_data, prediction = model[1].transform([text]), model[0].predict(model[1].transform([text]))
    return "Ham mail" if prediction[0] == 0 else "Spam mail"


if __name__ == "__main__":
    print(classify_text(input("text:")))

