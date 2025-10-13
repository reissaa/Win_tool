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

col1, col2 = st.columns(2)
img1=Image.open(Rf'site_info/{site}/暖冷房期間({site}).png')
with col1:
    folium.Marker(point,popup=site,icon=folium.Icon(color='red')).add_to(map)
    folium_static(map)
with col2:
   st.header("暖冷房期間")
   st.image(img1)
model=['標準住宅モデル','平屋モデル','3Fモデル']
Load=['General','Hiraya','3F']
def get_load_by_model(selected_model: str):
    model_to_load_map = {
        '標準住宅モデル': 'General',
        '平屋モデル': 'Hiraya',
        '3Fモデル': '3F'
    }
    return model_to_load_map.get(selected_model)
    

select_model =st.selectbox('想定モデル:',model)
sel_model=get_load_by_model(select_model)
col1, col2, col3 = st.columns(3)
img1=Image.open(Rf"png/{select_model}.png")

with col1:
    st.header("モデル")
    st.image(img1)
img2=Image.open(Rf"model_Load/{site}/{sel_model}/地点({site})・{sel_model}の年間月ごとの負荷・断熱等級4.png")
with col2:
    st.header("年間月ごと負荷")
    st.image(img2)
img3=Image.open(Rf"model_Load/{site}/{sel_model}//地点・{site}・モデル{sel_model}・年間月負荷割合.png")

with col3:
    st.header("割合")
    new_size = (10, 10)
    resized_img3 = img3.resize(new_size)
    st.image(img3)

col1, col2, col3 = st.columns(3)
img1=Image.open(Rf"png/標準住宅モデル窓面積表.png")
img_1=Image.open(Rf"png/標準住宅モデル窓面積割合.png")
with col1:
   st.header("方位ごとの窓面積")
   st.image(img1)
   st.header("窓面積割合")
   st.image(img_1)
img_2C=Image.open(Rf"site_info/{site}/冷房期間の4方位の日射量_地点({site}).png")
img_2H=Image.open(Rf"site_info/{site}/暖房期間の4方位の日射量_地点({site}).png")
with col2:
   st.header("冷房期間の日射量")
   st.image(img_2C)
   st.header("暖房期間の日射量")
   st.image(img_2H)
img3=Image.open(Rf"png/暖冷房スケジュール.png")
img4=Image.open(Rf"png/暖房冷房設定温度.png")
with col3:
   st.header("暖冷房スケジュール")
   st.image(img3)
   st.header("暖冷房の設定温度")
   st.image(img4)
