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
st.title('🪟Window Energy Performance')

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

    
    
    

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.title('南面のWEPH')
    st.markdown(f"{df_S[f'{select_winodow_s}'][0]:.2f}[kW/㎡・h]")
    st.title('南面のWEPC')
    st.markdown(f"{df_S[f'{select_winodow_s}'][1]:.2f}[kW/㎡・h]")


with col2:
    st.title('北面のWEPH')
    st.markdown(f"{df_N[f'{select_winodow_n}'][0]:.2f}[kW/㎡・h]")
    st.title('北面のWEPC')
    st.markdown(f"{df_N[f'{select_winodow_n}'][1]:.2f}[kW/㎡・h]")
    
with col3:
    st.title('東面のWEPH')
    st.markdown(f"{df_E[f'{select_winodow_e}'][0]:.2f}[kW/㎡・h]")
    st.title('東面のWEPC')
    st.markdown(f"{df_E[f'{select_winodow_e}'][0]:.2f}[kW/㎡・h]")
    
with col4:
    st.title('西面のWEPH')
    st.markdown(f"{df_W[f'{select_winodow_w}'][0]:.2f}[kW/㎡・h]")
    st.title('西面のWEPC')
    st.markdown(f"{df_W[f'{select_winodow_w}'][1]:.2f}[kW/㎡・h]")
    

WEP_Result=np.empty([2,4])
WEP_Result[0][0]=df_S[f'{select_winodow_s}'][0]*S_area
WEP_Result[1][0]=df_S[f'{select_winodow_s}'][1]*S_area
WEP_Result[0][1]=df_E[f'{select_winodow_e}'][0]*E_area
WEP_Result[1][1]=df_E[f'{select_winodow_e}'][1]*E_area
WEP_Result[0][2]=df_N[f'{select_winodow_n}'][0]*N_area
WEP_Result[1][2]=df_N[f'{select_winodow_n}'][1]*N_area
WEP_Result[0][3]=df_W[f'{select_winodow_w}'][0]*W_area
WEP_Result[1][3]=df_W[f'{select_winodow_w}'][1]*W_area
df=pd.DataFrame(WEP_Result)
df=df.T
df.columns=['WEPH[kW]','WEPC[kW]']
df.index=(['S','E','N','W'])



col_small, col_large = st.columns([1, 2])
with col_small:
    
    color=['crimson','darkorange','blue','darkgreen']
    fig, ax = plt.subplots()
    rate=[S_area,E_area,N_area,W_area]
    df_rate = pd.DataFrame(rate)
    fig = px.pie(df_rate, values=rate,names=['S','E','N','W'], title='窓面積の割合',color_discrete_sequence=color)
    st.plotly_chart(fig)
with col_large:
    color_1=['crimson','blue']
    
    

    st.bar_chart(df,color=color_1,horizontal=True)
    
    



