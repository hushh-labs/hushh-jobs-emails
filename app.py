import streamlit as st
import pandas as pd 
import numpy as np 
import requests
#from test import obtained_access_token
# from test import login_google
# from test import auth_google

st.title('Hushh-emails')

st.write("Enter your query")
gmail_query= st.text_input("Query")



if st.button('Login to your google account'):

    requests.get(url= "http://127.0.0.1:8000/login/google")
    # print(login)

    # json=login.json()
    # access_token=json.get('access_token')
    # access_token = requests.get(url= "http://127.0.0.1:8000/login/google")
    # print(access_token)
    #"access_token":login["access_token"]

    #access_token= login["access_token"]
    # print(access_token)
   

    requests.get(url=f"http://127.0.0.1:8000/download/google/?q={gmail_query}")
    #requests.get(url=f"http://127.0.0.1:8000/test/google?q={gmail_query}")

    
#     json_data = {
#     "access_token":access_token,
#     "user_query": gmail_query,
# }
#     response = requests.post("http://127.0.0.1:8000/auth/google", json=json_data)
#     print(response)
    #query= requests.get(url="http://127.0.0.1:8000/auth/google")
    # token = login.text
    # fetch = requests.get(url= "http://127.0.0.1:8000/auth/google/?code={token}")


    #st.subheader(f"Response from API = {fetch.text}")



