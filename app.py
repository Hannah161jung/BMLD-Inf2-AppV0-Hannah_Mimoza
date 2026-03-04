import streamlit as st

st.set_page_config(page_title="Meine App", page_icon=":material/home:")

pg_home = st.Page("views/home.py", title="Home", icon=":material/home:", default=True)
pg_ph = st.Page("views/pH-Rechner.py", title="pH-Rechner", icon=":material/science:")

pg = st.navigation([pg_home, pg_ph])
pg.run()
