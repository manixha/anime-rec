import streamlit as st
import pickle
import pandas as pd

def recommend(mov):
    index = movie[movie['title'] == mov].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key = lambda x: x[1])[1:6]
     
        
    recommended_movies = []
    for i in movie_list:
        anime_id = i[0]
        recommended_movies.append(movie.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movie_list.pkl','rb'))
movie = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similar.pkl','rb'))
st.title("Anime Recommendation System")

selected_movie_name = st.selectbox('Select the movies you want to be recommend'
    ,movie['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

