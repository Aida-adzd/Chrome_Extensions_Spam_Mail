from flask import Flask, render_template, request
from email_classifier import get_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        email = request.form['email']
        result = get_text(email)
        
    elif result is None or result == "":
        result = None
    
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)

