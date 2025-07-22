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

def plot_horizontal_bars_with_error_plotly(df, label_col, mean_col, std_col):
    """
    平均値の高い順に、エラーバー付き横棒グラフを Plotly で表示する（Streamlit対応）

    Parameters:
        df (pd.DataFrame): データフレーム
        label_col (str): ラベル（変数名）を含む列の名前
        mean_col (str): 平均値を含む列の名前
        std_col (str): 標準偏差を含む列の名前

    Returns:
        fig (plotly.graph_objects.Figure): 横棒グラフのFigureオブジェクト
    """
    # 平均値の降順に並び替え
    df_sorted = df.sort_values(by=mean_col, ascending=False)

    # 色を指定：正なら青、負なら赤
    colors = ['blue' if val >= 0 else 'red' for val in df_sorted[mean_col]]

    # 横棒グラフ作成
    fig = go.Figure(go.Bar(
        x=df_sorted[mean_col],
        y=df_sorted[label_col],
        error_x=dict(type='data', array=df_sorted[std_col], visible=True),
        orientation='h',
        marker=dict(color=colors),
        hovertemplate=f'{label_col}: %{{y}}<br>{mean_col}: %{{x}}<br>{std_col}: %{{error_x.array}}<extra></extra>'
    ))

    fig.update_layout(
        title='平均値と標準偏差による横棒グラフ',
        xaxis_title='平均値',
        yaxis_title='変数',
        yaxis=dict(autorange='reversed'),  # 上から高い順に
        template='plotly_white',
        height=max(400, len(df_sorted) * 40)  # 変数の数に応じて高さを調整
    )

    return fig
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
    



col1, col2, col3, col4,col5 = st.columns(5)
with col1:
    st.title('窓面積の割合')
    color=['crimson','darkorange','blue','darkgreen']
    fig, ax = plt.subplots()
    rate=[S_area,E_area,N_area,W_area]
    ax.pie(rate,colors=color,startangle=90)
WEP_Result=np.empty([2,4])
WEP_Result[0][0]=df_S[f'{select_winodow_s}'][0]
WEP_Result[1][0]=df_S[f'{select_winodow_s}'][1]
WEP_Result[0][1]=df_E[f'{select_winodow_e}'][0]
WEP_Result[1][1]=df_E[f'{select_winodow_e}'][1]
WEP_Result[0][2]=df_N[f'{select_winodow_n}'][0]
WEP_Result[1][2]=df_N[f'{select_winodow_n}'][1]
WEP_Result[0][3]=df_W[f'{select_winodow_w}'][0]
WEP_Result[1][3]=df_W[f'{select_winodow_w}'][1]
df=pd.DataFrame(WEP_Result)
df.columns=['S','E','N','W']
df.set_index=['WEPH[kW/㎡・h]','WEPC[kW/㎡・h]']
df=df.T
st.dataframe(df)
with col2:
    st.title('WEP＿Total')
    fig = plot_horizontal_bars_with_error_plotly(df)
    st.plotly_chart(fig, use_container_width=True)
