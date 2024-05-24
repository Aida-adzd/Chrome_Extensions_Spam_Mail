from flask import Flask, render_template, request, jsonify
from main import classify_text
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
CORS(app)


@app.route('/')
def home():
    return render_template('popup.html')


@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_json()
    if 'email' in data:
        email_text = data.get('email')
        result = classify_text(email_text)
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'No email text provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
