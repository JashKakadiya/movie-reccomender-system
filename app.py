from http.client import responses
from optparse import Option
import pickle
from urllib import response
from soupsieve import select
import streamlit as st
import pickle
import pandas as pd
import requests

up_df = pd.read_pickle(r"movies.pkl")
sim = pd.read_pickle(r"sim.pkl")
   
def rec(movie):
    inde = up_df[up_df['title'] == movie].index[0]
    dis = sim[inde]
    movie_list = sorted(list(enumerate(dis)),reverse=True ,key=lambda x:x[1])[1:6]
    LIST_IMAGE = []
    LIST_HEAD = []
    for i in movie_list:
        head = up_df.iloc[i[0]].title
        response = requests.get('https://api.themoviedb.org/3/movie/{}.id?api_key=0fae660bca9750db32843281ed11f25e&language=en-US'.format(up_df.iloc[i[0]].id))
        data = response.json()
        data2 = "https://image.tmdb.org/t/p/w500/"+ data['poster_path']
        LIST_IMAGE.append(data2)
        LIST_HEAD.append(head)
    return LIST_HEAD,LIST_IMAGE



st.title("Movie Recommendation System")
st.subheader("Feels like watching a movie to Enjoy & Chill, but are not sure what movie to select?")
st.markdown("Here's a easy peasy way to do it!  Best movie recommendations according to your Mood & Favourite Genre, is at your fingertips")

select = st.selectbox(
    'Choose your movie',
    up_df['title'].values
)
if st.button('recommend'):
   HEAD,IMAGE=  rec(select)
   col1,col2,col3,col4,col5 = st.columns(5)
   with col1:
       st.text(HEAD[0])
       st.image(IMAGE[0])

   with col2:
       st.text(HEAD[1])
       st.image(IMAGE[1])


   with col3:
       st.text(HEAD[2])
       st.image(IMAGE[2])


   with col4:
       st.text(HEAD[3])
       st.image(IMAGE[3])

       
   with col5:
       st.text(HEAD[4])
       st.image(IMAGE[4])
                                   
   
    

