import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Grade Horária - Eliane Potiguara", page_icon="🕒",layout="wide")

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="Turma - ELIANE POTIGUARA")

st.dataframe(df)
