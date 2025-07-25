import pandas as pd
import streamlit as st

from utils import load_data

st.title("Tabela com dados a serem usados")

df = load_data()

st.subheader("Dados Brutos de Nerlove - “Returns to Scale in Electricity Supply” (1963)")
st.dataframe(df.head())