
import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from datetime import datetime

st.set_page_config(page_title="Avisos", page_icon="⚠️",layout="wide")
sheet_url = st.secrets["SPREADSHEET"]

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="Avisos",spreadsheet=sheet_url)

st.dataframe(df,use_container_width=True,hide_index=True)
