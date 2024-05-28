from flask import Flask, render_template, request, jsonify
from email_classifier import EmailClassifier
from flask_cors import CORS
from conf import csv_file_path, model_path, popup_html

app = Flask(__name__, template_folder='templates')
CORS(app)

classifier = EmailClassifier(model_path, csv_file_path)

@app.route('/')
def home():
    return render_template(popup_html)

@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_json()
    if 'email' in data:
        email_text = data.get('email')
        result = classifier.classify(email_text)
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'No email text provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)