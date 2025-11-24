import plotly.express as px
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio
from streamlit_plotly_events import plotly_events
Win_df=pd.read_csv(R'窓性能ラベル/窓表作成.csv', header=0,sep=',',engine='python',encoding='cp932')
# Writes a component similar to st.write()

fig =px.scatter(Win_df, x="熱貫流率", y="日射熱取得率",hover_name='窓の種類')
fig.update_yaxes(range=(0,1))
fig.update_yaxes(tick0=0,dtick=0.1)
fig.update_xaxes(range=(0,6.0+0.11))
fig.update_xaxes(tick0=0,dtick=0.5)
#st.plotly_chart(fig)
selected_points = plotly_events(fig, click_event=True, hover_event=True)
#selected_points = plotly_events(fig)

# Can write inside of things using with!
#with st.expander('Plot'):
    #fig = px.line(x=[1], y=[1])
    #selected_points = plotly_events(fig, key="event_page_plotly_selector")

# Select other Plotly events by specifying kwargs
#fig = px.line(x=[1], y=[1])
#selected_points = plotly_events(fig, click_event=False, hover_event=True)
