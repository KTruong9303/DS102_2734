import streamlit as st
import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns

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
    ax.hist(df[col], bins=20)
    plt.xlabel(col)
    plt.ylabel('Quantity')
    st.pyplot(fig)

  st.header('show colleration')
  fig, ax = plt.subplots()
  sns.heatmap(df.corr(method='pearson'), ax=ax, vmax=1, square=True, annot=True, cmap='Blues')
  st.write(fig)

  output = st.radio('choose a dependent varaiable', df.columns)
  
  st.header('show relationship')
  for col in list(df.columns):
    if col != ouput:
      fig, ax = plt.subplots()
      ax.scatter(x=df[col], y=df[output])
      ax.hist(df[col], bins=20)
      plt.xlabel(col)
      plt.ylabel(output)
      st.pyplot(fig)
