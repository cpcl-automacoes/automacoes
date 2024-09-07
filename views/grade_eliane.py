import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from datetime import datetime

st.set_page_config(page_title="Grade Horária - Eliane Potiguara", page_icon="🕒",layout="wide")

sheet_url = st.secrets["spreadsheet"]
st.write(sheet_url)
