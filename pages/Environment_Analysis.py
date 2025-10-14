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

st.title('🔎あなたの住まいの気候区分と日射区分')

st.sidebar.success('項目を選択してください')
location=os.listdir(R'Env_analysis')
select_location =st.selectbox('地域を選択してください:',location)
point_data=pd.read_csv(Rf'site_data/地点の緯度経度.csv',index_col=None, header=0,sep=',',engine='python')
site=str(select_location)
point=list(point_data[site])
area_data=pd.read_csv(Rf'site_data/省エネ区分・日射区分(47site.ver).csv',index_col=None, header=0,sep=',',engine='python')
AREA=select_area=area_data[site][0]
Rad_AREA=select_area=area_data[site][1]
st.header(f"気候区分：{AREA}・日射区分:{Rad_AREA}")
map = folium.Map(location=point,zoom_start=4.7)

col1, col2, col3= st.columns(3)
img1=Image.open(Rf"Env_analysis/{site}/{site}(外気温度).png")
img2=Image.open(Rf"Env_analysis/{site}/{site}(相対湿度).png")
with col1:
    folium.Marker(point,popup=site,icon=folium.Icon(color='red')).add_to(map)
    folium_static(map,width=350, height=300)
with col2:
   st.header("外気温度[℃]")
   st.image(img1)
with col3:
   st.header("相対湿度[%]")
   st.image(img2)

col1, col2= st.columns(2)
img3=Image.open(Rf"Env_analysis/{site}/外気温度・相対湿度地点：{site}.png")
img4=Image.open(Rf"Env_analysis/{site}/日射量地点：{site}.png")
with col1:
    st.header("最高気温・平均気温・最低気温・平均相対湿度")
    st.image(img3)
with col2:
    st.header("日射＜法線面直達日射・水平面天空日射＞")
    st.image(img4)

st.header(f"{site} 風配図")
col1, col2,col3,col4,col5,col6= st.columns(6)
img5=Image.open(Rf"Env_analysis/{site}/風配図/1月の風配図  地点：{site}.png")
img6=Image.open(Rf"Env_analysis/{site}/風配図/2月の風配図  地点：{site}.png")
img7=Image.open(Rf"Env_analysis/{site}/風配図/3月の風配図  地点：{site}.png")
img8=Image.open(Rf"Env_analysis/{site}/風配図/4月の風配図  地点：{site}.png")
img9=Image.open(Rf"Env_analysis/{site}/風配図/5月の風配図  地点：{site}.png")
img10=Image.open(Rf"Env_analysis/{site}/風配図/6月の風配図  地点：{site}.png")


with col1:
    st.header("1月")
    st.image(img5)
with col2:
    st.header("2月")
    st.image(img6)
with col3:
    st.header("3月")
    st.image(img7)
with col4:
    st.header("4月")
    st.image(img8)
with col5:
    st.header("5月")
    st.image(img9)
with col6:
    st.header("6月")
    st.image(img10)

img11=Image.open(Rf"Env_analysis/{site}/風配図/1月の風配図  地点：{site}.png")
img12=Image.open(Rf"Env_analysis/{site}/風配図/2月の風配図  地点：{site}.png")
