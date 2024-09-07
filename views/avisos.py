
import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from datetime import datetime

st.set_page_config(page_title="Avisos", page_icon="📢",layout="wide")
sheet_url = st.secrets["SPREADSHEET"]

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="Avisos",spreadsheet=sheet_url)

col1, col2 = st.columns([2,1],vertical_alignment="center")

with col1:
    st.title("Avisos")

with col2:
  st.image("assets/logo_com_texto.png",use_column_width="auto")

for row in df:
  st.write(row["Avisos"])
