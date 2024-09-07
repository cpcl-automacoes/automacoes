import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Grade Horária - Lélia González", page_icon="🕒",layout="wide")

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="Turma - LÉLIA GONZÁLEZ")

st.dataframe(df)
