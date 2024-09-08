import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from datetime import datetime

st.set_page_config(page_title="Aulas por professor", page_icon="🕒",layout="wide")
sheet_url = st.secrets["SPREADSHEET"]

conn = st.connection("gsheets", type=GSheetsConnection)
df_lelia = conn.read(worksheet="Turma - LÉLIA GONZÁLEZ",spreadsheet=sheet_url)
df_eliane = conn.read(worksheet="Turma - ELIANE POTIGUARA",spreadsheet=sheet_url)

df = pd.concat([df_lelia,df_eliane])

df['Data'] = pd.to_datetime(df['Data'],format="%d/%m/%Y")

# Get today's date
today = pd.to_datetime(datetime.today().strftime('%d/%m/%Y'), format='%d/%m/%Y')

# Filter rows where the date is equal or greater than today
filtered_df = df[df['Data'] >= today]

filtered_df['Data'] = filtered_df['Data'].dt.strftime('%d/%m/%Y')

# Melt the dataframe to reshape it
df_melted = pd.melt(filtered_df, id_vars=['Data'], var_name='Horário da Aula', value_name='Aula')

# Renaming columns for clarity
df_melted.rename(columns={'Data': 'Data da Aula',"Horário da Aula":"Horário","Aula":"Professor"}, inplace=True)
df_melted = df_melted.loc[(df_melted["Professor"] != "INTERVALO") & (df_melted["Professor"] != "ALMOÇO")]
professores = df_melted["Professor"].sort_values().unique()

col1, col2 = st.columns([2,1],vertical_alignment="center")

with col1:
    st.title("Grade Horária por Professor")

with col2:
  st.image("assets/logo_com_texto.png",use_column_width="auto")


professor_select = st.multiselect(
    label="Selecione o professor",
    options = professores,
    default=None,
    placeholder = "Selecione o professor"
)

df_melted = df_melted.drop_duplicates()

selected_df = df_melted.loc[df_melted["Professor"] == professor_select]
st.dataframe(selected_df,use_container_width=True,hide_index=True)
