
import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from datetime import datetime

st.set_page_config(page_title="Grade Horária - Eliane Potiguara", page_icon="🕒",layout="wide")
sheet_url = st.secrets["SPREADSHEET"]

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="Turma - ELIANE POTIGUARA",spreadsheet=sheet_url)

df['Data'] = pd.to_datetime(df['Data'],format="%d/%m/%Y")

# Get today's date
today = pd.to_datetime(datetime.today().strftime('%d/%m/%Y'), format='%d/%m/%Y')

# Filter rows where the date is equal or greater than today
filtered_df = df[df['Data'] >= today]

filtered_df['Data'] = filtered_df['Data'].dt.strftime('%d/%m/%Y')

datas = filtered_df["Data"]

menor_data = filtered_df["Data"].min()

col1, col2 = st.columns([2,1],vertical_alignment="center")

with col1:
    st.title("Grade Horária - Eliane Potiguara")

with col2:
  st.image("assets/logo_com_texto.png",use_column_width="auto")

data_select = st.selectbox(
    label="Selecione a data",
    options = datas,
    placeholder = menor_data
)

selected_df = filtered_df.loc[filtered_df["Data"] == data_select]

selected_df = selected_df[selected_df.columns[1:]].transpose().reset_index()

selected_df.columns = ["Horário","Disciplina"]

st.dataframe(selected_df,use_container_width=True,hide_index=True,height=500)
