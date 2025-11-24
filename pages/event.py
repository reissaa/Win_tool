import plotly.express as px
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_plotly_events import plotly_events
df_S=pd.read_csv('WEP_Result47_4dir/TOKYO/direct_select/S/WEP_Result_TOKYO_S.csv', header=0,sep=',',engine='python')
# Writes a component similar to st.write()
df_S=df_S.T
df_S.columns=['WEP_H','WEP_C']
fig = px.scatter(df_S)
selected_points = plotly_events(fig)

# Can write inside of things using with!
#with st.expander('Plot'):
    #fig = px.line(x=[1], y=[1])
    #selected_points = plotly_events(fig, key="event_page_plotly_selector")

# Select other Plotly events by specifying kwargs
#fig = px.line(x=[1], y=[1])
#selected_points = plotly_events(fig, click_event=False, hover_event=True)
