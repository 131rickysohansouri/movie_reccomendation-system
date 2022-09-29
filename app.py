from urllib import response
import streamlit as st
import pickle
import pandas as pd
import requests
import json



def fetch_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=214be3ef00ee375c32d039fc7b209b08&language=en-US".format(movie_id))
    data=response.json()
    return 'https://image.tmdb.org/t/p/w500'+data['poster_path']



def reccomend(movie):
    index=movies[movies["title"] == movie].index[0]
    distances = sim[index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recom_movies=[]
    recom_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].id
        recom_movies.append(movies.iloc[i[0]].title)
        recom_posters.append(fetch_poster(movie_id))

    return recom_movies,recom_posters

movies_dict=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_dict)
sim=pickle.load(open('sim.pkl','rb'))




st.title("Movie Reccomendation system")
selected_movie_name = st.selectbox("Movies are",movies['title'].values)

if st.button("Reccomend"):
    reccomendations,posters=reccomend(selected_movie_name)
    # print(reccomendations)
    # for i in reccomendations:
    #     st.write(i)

    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:

        st.text(reccomendations[0])
        st.image(posters[0])

    with col2:
        st.text(reccomendations[1])
        st.image(posters[1])

    with col3:
        st.text(reccomendations[2])
        st.image(posters[2])

    with col4:
        st.text(reccomendations[3])
        st.image(posters[3])

    with col5:
        st.text(reccomendations[4])
        st.image(posters[4])

#lol