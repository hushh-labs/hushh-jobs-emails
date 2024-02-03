import streamlit as st
import pandas as pd 
import numpy as np 
import requests




st.title('Hushh-emails')

st.write("Enter your query")
gmail_query= st.text_input("Query")

if st.button('Login to your google account'):

    requests.get(url= "http://127.0.0.1:8000/login/google")

if st.button('Download resumes'):
    requests.get(url=f"http://127.0.0.1:8000/download/google?q={gmail_query}")

