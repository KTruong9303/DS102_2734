import streamlit as st
import pandas as pd
import io
import matplotlib.pyplot as plt

st.title('hola!')

st.header('up file')
data_file = st.file_uploader('choose file', type=(['.csv']))

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

  st.header('visualize')
  for col in list(df.columns):
    fig, ax = plt.subplots()
    ax.hist(df[col], bin=20)
    plt.xlabel(col)
    plt.ylabel('Quantity')
    st.pyplot(fig)
