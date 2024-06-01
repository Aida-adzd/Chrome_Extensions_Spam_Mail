from flask import Flask, render_template, request, jsonify
from email_classifier import EmailClassifier
from flask_cors import CORS
from conf import csv_file_path, model_path, popup_html  # Import paths from conf.py

# Create a Flask application
app = Flask(__name__, template_folder='templates')

# Enable Cross-Origin Resource Sharing (CORS) with Flask-CORS
CORS(app)

# Initialize the email classifier with the model and CSV file paths
classifier = EmailClassifier(model_path, csv_file_path)

@app.route('/')
def home():
    """
    Route for the home page.
    Renders the popup.html template.
    """
    return render_template(popup_html)

@app.route('/classify', methods=['POST'])
def classify():
    """
    Route for classifying an email text.
    Expects a JSON object in the request body with a key 'email'.
    Returns a JSON object with a key 'result' if classification is successful,
    or a key 'error' if an error occurs.
    """
    # Get the data from the request
    data = request.get_json()

    # Check if 'email' is in the data
    if 'email' in data:
        email_text = data.get('email')

        try:
            # Classify the email text
            result = classifier.classify(email_text)
            return jsonify({'result': result})
        except Exception as e:
            # Handle any errors that occur during classification
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'No email text provided'}), 400

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)