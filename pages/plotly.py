import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from streamlit_plotly_events import plotly_events

fig = make_subplots()
fig.add_trace(go.Scattergl(x=[1,2,3,4,5,6], y=[1,2,3,4,5,6]))
fig.update_layout(width=1100)
#st.plotly_chart(fig, template=‘plotly_white’)
selected_click = plotly_events(fig, click_event=True,hover_event=False)
st.write("選択された点:", selected_click )
