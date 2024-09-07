import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from datetime import datetime

st.set_page_config(page_title="Grade Horária - Lélia González", page_icon="🕒",layout="wide")

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="Turma - LÉLIA GONZÁLEZ")

df['Data'] = pd.to_datetime(df['Data'],format="%d/%m/%Y")

# Get today's date
today = pd.to_datetime(datetime.today().strftime('%d/%m/%Y'), format='%d/%m/%Y')

# Filter rows where the date is equal or greater than today
filtered_df = df[df['Data'] >= today]

filtered_df['Data'] = filtered_df['Data'].dt.strftime('%d/%m/%Y')

datas = filtered_df["Data"]

menor_data = filtered_df["Data"].min()

data_select = st.selectbox(
    label="Selecione a data",
    options = datas,
    placeholder = menor_data
)

selected_df = filtered_df.loc[filtered_df["Data"] == data_select]

st.dataframe(selected_df)
