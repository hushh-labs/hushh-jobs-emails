import streamlit as st
import pandas as pd 
import numpy as np 
import requests
from test import login_google
from test import auth_google

st.title('Hushh-emails')

st.write("Enter your query")

if st.button('Login to your google account'):
    login = requests.get(url= "http://127.0.0.1:8000/login/google")
    token = login.text
    fetch = requests.get(url= "http://127.0.0.1:8000/auth/google/?code={token}")


    st.subheader(f"Response from API = {fetch.text}")



