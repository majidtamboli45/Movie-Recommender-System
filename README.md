# 🎬 Movie Recommender System

A Content-Based Movie Recommender System built using Machine Learning and deployed on Streamlit Cloud.

🔗 **Live App:**  
https://movie-recommender-system-hnh8n4d4erjlcdrteqw5b8.streamlit.app/

---

## 📌 Project Overview

This project recommends movies similar to a selected movie using Natural Language Processing (NLP) and Cosine Similarity.

The system analyzes movie metadata such as genres, cast, crew, keywords, and overview to compute similarity scores and suggest the top 5 most similar movies.

---

## 🚀 Features

- Select a movie from a dropdown list
- Get Top 5 similar movie recommendations
- Content-based filtering approach
- Fast similarity computation
- Clean and interactive UI using Streamlit
- Deployed publicly on Streamlit Cloud
- Large similarity matrix hosted externally (Hugging Face)

---

## 🧠 How It Works

1. Dataset Used: TMDB 5000 Movies Dataset
2. Performed data cleaning and preprocessing
3. Combined important features:
   - Genres
   - Keywords
   - Cast
   - Crew
   - Overview
4. Created a combined text feature (`tags`)
5. Applied:
   - CountVectorizer (Bag of Words model)
   - Cosine Similarity
6. Generated similarity matrix
7. Built interactive UI using Streamlit
8. Deployed using GitHub + Streamlit Cloud

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Hugging Face (for large file hosting)
- GitHub

---

## 📂 Project Structure

movie-recommender-system/
│
├── app.py
├── movies.pkl
├── requirements.txt
├── README.md


> The similarity matrix file is hosted externally due to GitHub file size limitations and is automatically downloaded during app startup.

---

## ⚙️ Run Locally

```bash
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system
pip install -r requirements.txt
streamlit run app.py
📈 Future Improvements

Add movie posters using TMDB API

Add search-based recommendations

Implement collaborative filtering

Improve UI/UX design

Optimize similarity computation for faster loading
It Is The First Fully Developed Project By me