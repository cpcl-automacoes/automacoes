import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Grade Horária - Lélia González", page_icon="🕒",layout="wide")

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="Turma - LÉLIA GONZÁLEZ")

df['Data'] = pd.to_datetime(df['Data'],format="%d/%m/%Y")

# Get today's date
today = pd.to_datetime(datetime.today().strftime('%d/%m/%Y'))

# Filter rows where the date is equal or greater than today
filtered_df = df[df['Data'] >= today]
datas = df["Data"]

menor_data = filtered_df["Data"].min()

data_select = st.selectbox(
    label="Selecione a data",
    options = datas,
)

selected_df = filtered_df.loc[filtered_df["Data"] == data_select]

st.dataframe(selected_df)
