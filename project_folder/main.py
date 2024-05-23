from joblib import load


def load_model():
    # Load the model from the file
    model, feature_extraction = load('model.joblib')
    return model, feature_extraction


def resualt(text):
    model = load_model()
    input_data = model[1].transform([text])
    prediction = model[0].predict(input_data)

    if prediction[0] == 0:
        return "Ham mail"
    else:
        return "Spam mail"


if __name__ == "__main__":
    resualt(input("text:"))

