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
st.set_page_config(
    page_title='Multipage App',
    page_icon='🗾',
    layout='wide',
)
st.title('🪟Window Energy Performance')
st.title('Plan1')
location=os.listdir(R'Win_tool_47')
df_0=pd.read_csv(R'Window_info/窓表作成.csv', header=0,sep=',',engine='python',encoding='cp932')
window_selectS=df_0['窓の種類']
window_selectE=df_0['窓の種類']
window_selectN=df_0['窓の種類']
window_selectW=df_0['窓の種類']
select_location =st.sidebar.selectbox('地域を選択してください', location)
select_winodow_s =st.sidebar.selectbox('南の窓の種類を選択', window_selectS)
S_area = st.sidebar.slider("南面の窓面積を入力", 0, 40, 25)
select_winodow_e =st.sidebar.selectbox('東の窓の種類を選択', window_selectE)
E_area = st.sidebar.slider("東面の窓面積を入力", 0, 40, 25)
select_winodow_n =st.sidebar.selectbox('北の窓の種類を選択', window_selectN)
N_area = st.sidebar.slider("北面の窓面積を入力", 0, 40, 25)
select_winodow_w =st.sidebar.selectbox('西の窓の種類を選択', window_selectW)
W_area = st.sidebar.slider("西面の窓面積を入力", 0, 40, 25)
df_S=pd.read_csv(f'WEP_Result47_4dir/{select_location}/direct_select/S/WEP_Result_{select_location}_S.csv', header=0,sep=',',engine='python')
df_E=pd.read_csv(f'WEP_Result47_4dir/{select_location}/direct_select/E/WEP_Result_{select_location}_E.csv', header=0,sep=',',engine='python')
df_N=pd.read_csv(f'WEP_Result47_4dir/{select_location}/direct_select/N/WEP_Result_{select_location}_N.csv', header=0,sep=',',engine='python')
df_W=pd.read_csv(f'WEP_Result47_4dir/{select_location}/direct_select/W/WEP_Result_{select_location}_W.csv', header=0,sep=',',engine='python')

df_E[f'{select_winodow_e}']
df_N[f'{select_winodow_n}']
df_W[f'{select_winodow_w}']

col1, col2, col3, col4,col5 = st.columns(5)
with col1:
    st.title('方位ごとの窓面積の割合')
    color=['crimson','darkorange','blue','darkgreen']
    fig, ax = plt.subplots()
    rate=[S_area,E_area,N_area,W_area]
    ax.pie(rate,colors=color,startangle=90)

    st.pyplot(fig)
with col2:
    st.title('WEP＿Total')
col1, col2, col3, col4 = st.columns(4)
sxa

with col1:
    st.title('南面のWEPH')
    st.markdown(f"{df_S[f'{select_winodow_s}'][0]:.2f}")
    st.title('南面のWEPC')
    st.markdown(f"{df_S[f'{select_winodow_s}'][1]:.2f}")


with col2:
    st.title('北面のWEPH')
    st.title('北面のWEPC')
    
with col3:
    st.title('東面のWEPH')
    st.title('東面のWEPC')
    
with col4:
    st.title('西面のWEPH')
    st.title('西面のWEPC')
st.title('Plan2')
