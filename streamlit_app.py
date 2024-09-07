import streamlit as st

# --- PAGE SETUP ---
page_eliane = st.Page(
    "views/grade_eliane.py",
    title="Eliane Potiguara",
    icon=":material/schedule:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Grade Horária": [page_eliane]
    }
)


# --- SHARED ON ALL PAGES ---
# st.logo("assets/codingisfun_logo.png")


# --- RUN NAVIGATION ---
pg.run()
