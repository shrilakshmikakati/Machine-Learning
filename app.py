import pickle
import streamlit as st
import requests



def recommend(movie):
    index = movies[movies['title']== movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key = lambda x:x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_name.append(movies.iloc[i[0]].title)
    return recommended_movies_name, recommended_movies_poster

st.header("Movie Recommendation system using Machine Learning")
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similaroty.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Type or select a movie to get recommendation',
    movie_list
    )

if st.button('show recommendation'):
    recommended_movie_name,recommended_movies_poster = recommend(selected_movie)
    row1,row2,row3,row4,row5 = st.columns(5)
    with row1:
        st.text(recommended_movie_name[0])
    with row2:
        st.text(recommended_movie_name[1])
    with row3:
        st.text(recommended_movie_name[2])
    with row4:
        st.text(recommended_movie_name[3]) 
    with row5:
        st.text(recommended_movie_name[4])