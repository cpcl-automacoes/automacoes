import streamlit as st

# --- PAGE SETUP --

page_avisos = st.Page(
    "views/avisos.py",
    title="avisos",
    icon=":material/campaign:",
    default= True
)
-
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
    title="Dia das aulas",
    icon=":material/school:",
)

# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Avisos": [page_avisos],
        "Turmas": [page_eliane,page_lelia],
        "Professores": [page_professores]
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("assets/logo_sem_texto.png")

# --- RUN NAVIGATION ---
pg.run()
