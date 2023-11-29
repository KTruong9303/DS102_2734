import streamlit as st
import pandas as pd
import io

st.title('hola!')

st.header('up file')
data_file = st.file_uploader('choose file', type=([.csv]))

if data_file is not None:
  df = pd.read_csv(data_file)
  st.header('show data')
  st.dataframe(df)
  st.header('statistic:')
  st.table(df.describe())

  st.header('Show data information')
  buffer = io.StringIO()
  df.info(buf=buffer)
  st.text(buffer.getvalue())
  
