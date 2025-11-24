import streamlit as st
import plotly.express as px

# データの作成
df = px.data.iris()

# Plotlyでグラフを作成
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')

# Streamlitで表示
st.plotly_chart(fig)
