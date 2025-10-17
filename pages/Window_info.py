import streamlit as st
import pandas as pd
import numpy as np
from math import pi
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static
import plotly.express as px
import altair as alt
from PIL import Image
import os
import plotly.graph_objects as go





st.set_page_config(
    page_title='Multipage App',
    page_icon='🗾',
    layout='wide',
)
st.title('🪟Window information')

location=os.listdir(R'site_info/')
df_0=pd.read_csv(R'Window_info/窓表作成.csv', header=0,sep=',',engine='python',encoding='cp932')

win_name=list(df_0['窓の種類'])

col1, col2 = st.columns(2)
img1=Image.open(Rf"png/熱貫流率の分布.png")
img2=Image.open(Rf"png/日射熱取得率の分布.png")
with col1:
    st.header("断熱性能")
    st.image(img1)
with col2:
   st.header("日射取得性能")
   st.image(img2)
select_window=st.selectbox('窓を選択してください', win_name)
st.header(f"窓の性能　選択された窓{select_window}")
    
col1, col2 = st.columns(2)
img3=Image.open(Rf"窓性能ラベル/断熱性能/{select_window}.png")
img4=Image.open(Rf"窓性能ラベル/日射取得率/{select_window}.png")
with col1:
    st.header("断熱")
    st.image(img3)
with col2:
    st.header("日射取得")
    st.image(img4)
 
    
st.subheader('窓の性能比較📋')
ABC3 = st.multiselect(
    'Please select',
    win_name,
    [],
    max_selections=2,
    )


