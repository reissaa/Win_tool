import streamlit as st
import pandas as pd
import numpy as np
import os
import glob
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
location=os.listdir(R'site_info/')
select_location =st.sidebar.selectbox('地域を選択してください', location)
df_0=pd.read_csv(R'Window_info/窓表作成.csv', header=0,sep=',',engine='python',encoding='cp932')

win_name=list(df_0['窓の種類'])
Win_df=pd.read_csv(R'窓性能ラベル/窓表作成.csv', header=0,sep=',',engine='python',encoding='cp932')


dfS=pd.read_csv(f'WEP_Result47_4dir/{select_location}/direct_select/S/WEP_Result_{select_location}_S.csv', header=0,sep=',',engine='python')
dfS=dfS.T
dfS.reset_index(inplace=True, drop=True)
dfS.columns=['WEP_H','WEP_C']
S_df=pd.concat([Win_df,dfS],axis=1)

fig = px.scatter(S_df,x=S_df['熱貫流率'],y=S_df['日射熱取得率'], hover_name='窓の種類',color='WEP_H',hover_data='熱貫流率',color_continuous_scale=['green','yellow','orange','red'])
fig.update_yaxes(range=(0,1))
fig.update_yaxes(tick0=0,dtick=0.1)
fig.update_xaxes(range=(0,6.0+0.11))
fig.update_xaxes(tick0=0,dtick=0.5)
fig.update_layout(
    title="窓の熱貫流率と日射取得率",
    xaxis_title="熱貫流率[W/㎡・K]",  
    yaxis_title="日射取得率[-]",
   width=700,
    height=500,
    font=dict(size=26,
                color='grey'),
    
)
st.plotly_chart(fig)

fig = px.scatter(S_df,x=S_df['熱貫流率'],y=S_df['日射熱取得率'], hover_name='窓の種類',color='WEP_C',hover_data='熱貫流率',color_continuous_scale=['green','lightgreen','skyblue','blue'])
fig.update_yaxes(range=(0,1))
fig.update_yaxes(tick0=0,dtick=0.1)
fig.update_xaxes(range=(0,6.0+0.11))
fig.update_xaxes(tick0=0,dtick=0.5)
fig.update_layout(
    title="窓の熱貫流率と日射取得率",
    xaxis_title="熱貫流率[W/㎡・K]",  
    yaxis_title="日射取得率[-]",
   width=700,
    height=500,
    font=dict(size=26,
                color='grey'),
    
)
st.plotly_chart(fig)
st.subheader('窓の性能比較📋')
ABC = st.multiselect(
    'Please select',
    win_name,
    [],
    max_selections=2,
    )
st.write(ABC)
