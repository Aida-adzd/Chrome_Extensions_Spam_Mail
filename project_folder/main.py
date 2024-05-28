from email_classifier import EmailClassifier
from conf import csv_file_path


def main(classifier):
    print(classifier.classify(input("text:")))


if __name__ == "__main__":
    classifier = EmailClassifier('model.joblib', csv_file_path)
    main(classifier)
