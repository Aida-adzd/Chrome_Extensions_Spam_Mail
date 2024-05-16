# Email Classification - Ham or Spam

This project includes a Flask web application and a machine learning model for classifying emails as either ham (non-spam) or spam. Additionally, a Chrome extension is provided for convenient access to the classification service.

## Components

1. [Flask Web Application](#flask-web-application)
2. [Machine Learning Model](#machine-learning-model)
3. [Chrome Extension](#chrome-extension)
4. [Usage](#usage)
5. [Installation](#installation)

## Flask Web Application

### Purpose

The Flask web application serves as the user interface for email classification. Users can input an email, and the application will classify it as ham or spam using a machine learning model.

### File Structure

- `app.py`: Main file containing the Flask application, routes, and logic.
- `email_classifier.py`: Module providing functions for loading, preprocessing, training, and classifying emails using a machine learning model.
- `templates/index.html`: HTML template for the main webpage, including a form for entering an email and displaying the classification result.

### Functionality

1. User inputs an email on the webpage.
2. The input email is sent to the machine learning model for classification.
3. The classification result (ham or spam) is displayed on the webpage.

### Required Libraries

Make sure to install the required Python libraries for the Flask web application:

```bash
pip install Flask
pip install scikit-learn
```

## Machine Learning Model

### Purpose

The machine learning model is responsible for training and classifying emails as spam or ham.

### File Structure

- `machine_learning_model.py`: Python script for loading and preprocessing email data, training a Logistic Regression model, and evaluating its performance.
- `mail_data.csv`: CSV file containing labeled email data for training the machine learning model.

### Functionality

1. Load and preprocess labeled email data from `mail_data.csv`.
2. Train a Logistic Regression model with TF-IDF feature extraction.
3. Evaluate the model's performance.
4. Classify new emails as spam or ham using the trained model.

### Required Libraries

Ensure you have the required Python libraries installed for the machine learning model:

```bash
pip install pandas
pip install scikit-learn
```

## Chrome Extension

### Purpose

The Chrome extension provides a quick and easy way for users to interact with the email classification service directly from the browser.

### File Structure

- `manifest.json`: Manifest file specifying extension details, including permissions, icons, and popup behavior.
- `popup.html`: HTML file defining the structure of the extension's popup.
- `popup.js`: JavaScript file handling the logic for the extension's popup, including opening a new tab with the Flask web application.

### Functionality

1. Clicking the extension icon opens a popup with an option to check emails.
2. The popup is linked to the Flask web application, allowing users to quickly access the email classification service.

## Usage

1. **Flask Web Application:**
   - Run the Flask application using `python app.py`.
   - Open a web browser and visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
   - Enter an email to view the classification result.

2. **Machine Learning Model:**
   - Train and evaluate the machine learning model using the `machine_learning_model.py` script.
   - Customize the script or functions as needed for your specific use case.

3. **Chrome Extension:**
   - Load the extension in Chrome:
     1. Open Chrome and go to `chrome://extensions/`.
     2. Enable "Developer mode" at the top right.
     3. Click "Load unpacked" and select the extension folder.

## Installation

To set up the entire system, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Flask Web Application:**
   - Install dependencies:
     ```bash
     pip install Flask scikit-learn
     ```
   - Run the Flask application:
     ```bash
     python app.py
     ```
   - Open a web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. **Machine Learning Model:**
   - Train and evaluate the machine learning model using the `machine_learning_model.py` script.
   - Customize the script or functions as needed for your specific use case.

4. **Chrome Extension:**
   - Open Chrome and go to `chrome://extensions/`.
   - Enable "Developer mode" at the top right.
   - Click "Load unpacked" and select the extension folder.
