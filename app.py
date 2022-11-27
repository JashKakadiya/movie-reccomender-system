from http.client import responses
from optparse import Option
import pickle
from urllib import response
from soupsieve import select
import streamlit as st
import pickle
import pandas as pd
import requests
# movies_list = pickle(open('movies.pkl','rb'))
# load = movies_list['title'].values

up_df = pd.read_pickle(r"movies.pkl")
sim = pd.read_pickle(r"sim.pkl")



# def scroll(head,data):
#     ol1,col2,col3,col4,col5 = st.columns(5)
#     for ind in ['col1','col2','col3','col4','col5']:
#         st.write(ind)
#         with ind:
#             st.header(head)
#             st.image(data)
   
def rec(movie):
    inde = up_df[up_df['title'] == movie].index[0]
    dis = sim[inde]
    movie_list = sorted(list(enumerate(dis)),reverse=True ,key=lambda x:x[1])[1:6]
    # movie_id = up_df.iloc[i[0]].title
    for i in movie_list:
        head = up_df.iloc[i[0]].title
        # st.write(up_df.iloc[i[0]].id)
        response = requests.get('https://api.themoviedb.org/3/movie/{}.id?api_key=0fae660bca9750db32843281ed11f25e&language=en-US'.format(up_df.iloc[i[0]].id))
        # st.write(response)
        data = response.json()
        data2 = "https://image.tmdb.org/t/p/w500/"+ data['poster_path']
        st.header(head)
        st.image(data2)
        # return head,data2



st.title("Movie recommanded system")

select = st.selectbox(
    'how would ypu like to connect',
    up_df['title'].values
)
if st.button('reccomand'):
    rec(select)
    # scroll(head,data2)

