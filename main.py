import streamlit as st
import pandas as pd

st.title('hola!')

data_file = st.file_uploader('choose file', type=([.csv]))

if data_file is not None:
  df = pd.read_csv(data_file)

  st.dataframe(df)
