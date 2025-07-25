import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    data = pd.read_excel('data/Nerlove1963.xlsx')
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data