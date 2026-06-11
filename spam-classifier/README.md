# Spam Detection Web App

A Flask-based web application that detects whether a message is Spam or Not Spam using a trained machine learning model.

## Features

* Simple web interface
* Real-time spam prediction
* Machine learning model integration
* Flask backend

## Project Structure

```text
spam-classifier/
│
├── README.md
├── app.py
├── model.pkl
├── vectorizer.pkl
│
└── templates/
    └── index.html
```

## Requirements

* Python 3.x
* Flask
* Scikit-learn
* Pickle

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd spam-classifier
```

Install dependencies:

```bash
pip install flask scikit-learn
```

## Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## How It Works

1. User enters a message.
2. The message is converted into numerical features using `vectorizer.pkl`.
3. The trained model in `model.pkl` predicts whether the message is spam.
4. The result is displayed on the webpage.

## Files Description

* `app.py` - Flask application
* `model.pkl` - Trained spam classification model
* `vectorizer.pkl` - Text vectorizer
* `templates/index.html` - Frontend user interface

## Author
GUNDALA VARSHA

Your Name
