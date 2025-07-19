import streamlit as st

import pandas as pd
import numpy as np


from math import pi

import folium
from streamlit_folium import folium_static
import plotly.express as px
import altair as alt
from PIL import Image
import os
st.set_page_config(
    page_title='Multipage App',
    page_icon='🗾',
    layout='wide',
)

st.title('環境設計ツール')
st.sidebar.success('Select a page above')
location=os.listdir(R'Win_tool_47')
select_location =st.selectbox('地域を選択してください:',location)
point_data=pd.read_csv(Rf'site_data/地点の緯度経度.csv',index_col=None, header=0,sep=',',engine='python')
site=str(select_location)
point=list(point_data[site])
map = folium.Map(location=point,zoom_start=4.7,width=450,height=380)

col1, col2 = st.columns(2)
img1=Image.open(Rf'Win_tool_47/{site}/暖冷房期間({site}).png')
with col1:
    folium.Marker(point,popup=site,icon=folium.Icon(color='red')).add_to(map)
    folium_static(map)
with col2:
   st.header("暖冷房期間")
   st.image(img1)
st.title('あなたの住まいの省エネ区分と日射区分')




