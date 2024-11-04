import streamlit as st

# --- PAGE SETUP ---

st.set_page_config(
    page_title="Sharanya's Portfolio",
    layout="wide")


about_page = st.Page(
    "views/about_me.py",
    title="About Me",
    icon="🤖",
    default=True,
)






# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("assets/menu.gif")
st.sidebar.text("Made with ❤️ by Sharanya Akkenapally")


# --- RUN NAVIGATION ---
pg.run()