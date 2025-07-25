import streamlit as st

pg_tabela = st.Page('tabela.py', title="Tabela de dados", icon=":material/table:")
pg_grafico = st.Page('grafico.py', title="Gráficos dos dados", icon=":material/bar_chart:")

pg = st.navigation([pg_tabela, pg_grafico])
st.set_page_config(page_title='Amostragem básica de dados', layout='wide', page_icon=':material/folder:')
pg.run()
