import streamlit as st

# --- PAGE SETUP ---
page_eliane = st.Page(
    "views/grade_eliane.py",
    title="Eliane Potiguara",
    icon=":material/schedule:",
)

page_lelia = st.Page(
    "views/grade_lelia.py",
    title="Lélia González",
    icon=":material/schedule:",
)

page_professores = st.Page(
    "views/grade_professores.py",
    title="Dias das aulas",
    icon=":material/school:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Turma": [page_eliane,page_lelia],
        "Professores": [page_professores]
    }
)


# --- SHARED ON ALL PAGES ---
# st.logo("assets/codingisfun_logo.png")


# --- RUN NAVIGATION ---
pg.run()
