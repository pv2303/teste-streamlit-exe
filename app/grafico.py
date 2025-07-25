import streamlit as st

from tabela import df

st.subheader("Scatterplot entre cost e output")

st.scatter_chart(df, x = 'cost', y = 'output')

st.subheader('Scatterplot entre plabor e output')

st.scatter_chart(df, x = 'plabor', y = 'output')