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

st.title('🔎あなたの住まいの省エネ区分と日射区分')

st.sidebar.success('Select a page above')
location=os.listdir(R'Win_tool_47')
select_location =st.selectbox('地域を選択してください:',location)
point_data=pd.read_csv(Rf'site_data/地点の緯度経度.csv',index_col=None, header=0,sep=',',engine='python')
site=str(select_location)
point=list(point_data[site])
area_data=pd.read_csv(Rf'site_data/省エネ区分・日射区分(47site.ver).csv',index_col=None, header=0,sep=',',engine='python')
AREA=select_area=area_data[site][0]
Rad_AREA=select_area=area_data[site][1]
st.header(f"気候区分：{AREA}・日射区分:{Rad_AREA}")
map = folium.Map(location=point,zoom_start=4.7)

col1, col2 = st.columns(2)
img1=Image.open(Rf'Win_tool_47/{site}/暖冷房期間({site}).png')
with col1:
    folium.Marker(point,popup=site,icon=folium.Icon(color='red')).add_to(map)
    folium_static(map)
with col2:
   st.header("暖冷房期間")
   st.image(img1)
