import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from streamlit_plotly_events import plotly_events
import pandas as pd
Win_df=pd.read_csv(R'窓性能ラベル/窓表作成.csv',index_col=0, header=0,sep=',',engine='python',encoding='cp932')
fig = make_subplots()
fig.add_trace(go.Scatter(x=list(Win_df['熱貫流率']), y=list(Win_df['日射熱取得率']),mode="markers"))
fig.update_yaxes(range=(0,1))
fig.update_yaxes(tick0=0,dtick=0.1)
fig.update_xaxes(range=(0,6.0+0.11))
fig.update_xaxes(tick0=0,dtick=0.5)
#st.plotly_chart(fig, template=‘plotly_white’)
selected_click = plotly_events(fig, click_event=True)
st.write("選択された点:",selected_click)
