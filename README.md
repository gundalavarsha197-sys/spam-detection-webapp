# 📩 Spam Detection Web App

A Machine Learning-based web application that detects whether a given message is **Spam or Not Spam (Ham)** using Natural Language Processing and a trained ML model, deployed using Flask.

---

## 🚀 Features

* Predicts spam vs ham messages in real-time
* Simple and user-friendly web interface
* Machine Learning model trained on text data
* Flask-based backend for deployment
* Fast and lightweight predictions

---

## 🛠️ Technologies Used

* Python 🐍
* Flask 🌐
* Scikit-learn 🤖
* Pandas 📊
* Numpy
* HTML, CSS (Frontend)

---

## 📊 Machine Learning Process

1. Data collection (SMS/Email dataset)
2. Text preprocessing (cleaning, tokenization)
3. Feature extraction (TF-IDF / CountVectorizer)
4. Model training (Naive Bayes / Logistic Regression)
5. Deployment using Flask

---

## ⚙️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/spam-detection-webapp.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000
```

---

## 📸 Output

* Input message → Prediction result (Spam / Not Spam)
* <img width="1918" height="1078" alt="spam" src="https://github.com/user-attachments/assets/1b863a7a-9f13-4ec3-96e1-8c1f4a844170" />


---

## 🎯 Example

| Message                  | Prediction |
| ------------------------ | ---------- |
| "Win a free iPhone now!" | 🚨 Spam    |
| "Are we meeting today?"  | ✅ Not Spam |

---

## 📌 Project Structure

```
spam-detection-webapp/
│── app.py
│── model.pkl
│── vectorizer.pkl
│── templates/
│── static/
│── requirements.txt
```

---

## 👨‍💻 Author

GUNDALA VARSHA

---

## ⭐ Future Improvements

* Improve accuracy using deep learning
* Add email spam detection
* Deploy on cloud (Render/Heroku/AWS)
