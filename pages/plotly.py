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

Win_df=pd.read_csv(R'窓性能ラベル/窓表作成.csv', header=0,sep=',',engine='python',encoding='cp932')
df1=pd.read_csv(f'WEP_Result47_4dir/{select_location}/direct_select/S/WEP_Result_{select_location}_S.csv', header=0,sep=',',engine='python'))
fig = make_subplots()
fig.add_trace(go.Scatter(x=list(Win_df['熱貫流率']), y=list(Win_df['日射熱取得率']),mode="markers"))
fig.update_yaxes(range=(0,1))
fig.update_yaxes(tick0=0,dtick=0.1)
fig.update_xaxes(range=(0,6.0+0.11))
fig.update_xaxes(tick0=0,dtick=0.5)
#st.plotly_chart(fig, template=‘plotly_white’)
selected_click = plotly_events(fig, click_event=True)
st.write("選択された点:",selected_click)
