Movie Recommendation System

A Machine Learning-powered Web Application that recommends movies based on a user-selected movie. Built with Flask, Python, and Content-Based Filtering using TF-IDF + Cosine Similarity.

✨ Features
🎯 Recommend movies based on similarity
🔍 Search and select any movie from the dataset
⚡ Fast and responsive web interface
🌐 Built with Flask, fully interactive
🧠 Uses ML algorithms for recommendation
🧠 How It Works
Movie descriptions are converted into numerical vectors using TF-IDF vectorization
Cosine similarity measures how similar movies are
The system recommends top movies that are most similar to the selected movie

🛠️ Tech Stack
Python – Core programming language
Flask – Web framework
Pandas – Data handling
Scikit-learn – Machine Learning & TF-IDF
HTML / CSS – Frontend UI

📁 Project Structure
movie-recommender/
│
├── app.py                 # Flask backend
├── movies.csv             # Dataset
├── templates/
│   └── index.html         # Frontend UI
├── static/
│   └── style.css          # Custom styling
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
▶️ How to Run
1️⃣ Clone the Repository
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the Application
python app.py
4️⃣ Open in Browser
http://127.0.0.1:5000/

🎯 Example
Input: Avengers
Recommendations:

Iron Man
Spider Man
Thor
Batman Begins

🌟 Future Enhancements
Add TMDB / MovieLens API integration for real-time movie data
Display movie posters dynamically
Add user ratings & collaborative filtering
Deploy online using Render / Railway / Heroku

🏆 Learning Outcomes
Build a content-based recommendation system
Understand TF-IDF vectorization & cosine similarity
Learn Flask web development for ML apps
Integrate ML model with interactive frontend

👨‍💻 Author

GUNDALA VARSHA
GitHub: 
LinkedIn:Gundala Varsha
