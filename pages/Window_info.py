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
import plotly.express as px
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio
from streamlit_plotly_events import plotly_events




st.set_page_config(
    page_title='Multipage App',
    page_icon='🗾',
    layout='wide',
)
st.title('🪟Window information')

location=os.listdir(R'site_info/')
df_0=pd.read_csv(R'Window_info/窓表作成.csv', header=0,sep=',',engine='python',encoding='cp932')

win_name=list(df_0['窓の種類'])

Win_df=pd.read_csv(R'窓性能ラベル/窓表作成.csv', header=0,sep=',',engine='python',encoding='cp932')
# Writes a component similar to st.write()
fig =px.scatter(Win_df,x=Win_df["熱貫流率"],y=Win_df["日射熱取得率"],hover_name='窓の種類')

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

select_window=st.selectbox('窓を選択してください', win_name)
st.write(f"窓の性能　選択された窓{select_window}")
    
col1, col2 = st.columns(2)
img3=Image.open(Rf"窓性能ラベル/断熱性能/{select_window}.png")
img4=Image.open(Rf"窓性能ラベル/日射取得率/{select_window}.png")
with col1:
    st.header("断熱")
    st.image(img3)
with col2:
    st.header("日射取得")
    st.image(img4)
 
    


