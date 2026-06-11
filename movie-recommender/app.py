from flask import Flask, render_template, request
import pandas as pd
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

API_KEY = "YOUR_TMDB_API_KEY"

df = pd.read_csv("movies.csv")

tfidf = TfidfVectorizer(stop_words='english')
matrix = tfidf.fit_transform(df["genre"])
similarity = cosine_similarity(matrix)

def fetch_poster(movie):
    try:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie}"
        data = requests.get(url).json()
        poster_path = data['results'][0]['poster_path']
        return "https://image.tmdb.org/t/p/w500" + poster_path
    except:
        return ""

def recommend(movie):
    if movie not in df["title"].values:
        return [], []

    idx = df[df["title"] == movie].index[0]
    scores = list(enumerate(similarity[idx]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]

    recommended_movies = []
    posters = []

    for i in sorted_scores:
        title = df.iloc[i[0]]["title"]
        recommended_movies.append(title)
        posters.append(fetch_poster(title))

    return recommended_movies, posters

@app.route("/")
def home():
    return render_template("index.html", movies=df["title"].tolist())

@app.route("/recommend", methods=["POST"])
def get_recommendation():
    movie = request.form["movie"]
    names, posters = recommend(movie)

    return render_template("index.html",
                           movies=df["title"].tolist(),
                           selected=movie,
                           names=names,
                           posters=posters)

if __name__ == "__main__":
    app.run(debug=True)