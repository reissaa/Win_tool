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
st.title('南面のWEPの比較')
select_location =st.sidebar.selectbox('地域を選択してください', location)
df_0=pd.read_csv(R'Window_info/窓表作成.csv', header=0,sep=',',engine='python',encoding='cp932')

win_name=list(df_0['窓の種類'])
Win_df=pd.read_csv(R'窓性能ラベル/窓表作成.csv', header=0,sep=',',engine='python',encoding='cp932')
df_S=pd.read_csv(f'WEP_Result47_4dir/{select_location}/direct_select/S/WEP_Result_{select_location}_S.csv', header=0,sep=',',engine='python')
df_E=pd.read_csv(f'WEP_Result47_4dir/{select_location}/direct_select/E/WEP_Result_{select_location}_E.csv', header=0,sep=',',engine='python')
df_N=pd.read_csv(f'WEP_Result47_4dir/{select_location}/direct_select/N/WEP_Result_{select_location}_N.csv', header=0,sep=',',engine='python')
df_W=pd.read_csv(f'WEP_Result47_4dir/{select_location}/direct_select/W/WEP_Result_{select_location}_W.csv', header=0,sep=',',engine='python')

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
    title=Rf"WEP_Heating ",
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
    title=f"WEP_Cooling ",
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
    '窓を2つ選択してください',
    win_name,
    [],
    max_selections=2,
    )
st.write(ABC[0])
st.write(ABC[1])
Win1=ABC[0]
Win2=ABC[1]
WEP_ResultH=np.empty([2,4])
WEP_ResultH[0][0]=df_S[f'{Win1}'][0]
WEP_ResultH[1][0]=df_S[f'{Win2}'][0]
WEP_ResultH[0][1]=df_E[f'{Win1}'][0]
WEP_ResultH[1][1]=df_E[f'{Win2}'][0]
WEP_ResultH[0][2]=df_N[f'{Win1}'][0]
WEP_ResultH[1][2]=df_N[f'{Win2}'][0]
WEP_ResultH[0][3]=df_W[f'{Win1}'][0]
WEP_ResultH[1][3]=df_W[f'{Win2}'][0]
Hdf=pd.DataFrame(WEP_ResultH)
Hdf=Hdf.T
Hdf.columns=[f'{Win1}',f'{Win2}']
Hdf.index=(['S','E','N','W'])
st.write(Hdf)

WEP_ResultC=np.empty([2,4])
WEP_ResultC[0][0]=df_S[f'{Win1}'][1]
WEP_ResultC[1][0]=df_S[f'{Win2}'][1]
WEP_ResultC[0][1]=df_E[f'{Win1}'][1]
WEP_ResultC[1][1]=df_E[f'{Win2}'][1]
WEP_ResultC[0][2]=df_N[f'{Win1}'][1]
WEP_ResultC[1][2]=df_N[f'{Win2}'][1]
WEP_ResultC[0][3]=df_W[f'{Win1}'][1]
WEP_ResultC[1][3]=df_W[f'{Win2}'][1]
Cdf=pd.DataFrame(WEP_ResultC)
Cdf=Cdf.T
Cdf.columns=[f'{Win1}',f'{Win2}']
Cdf.index=(['S','E','N','W'])
st.write(Cdf)
Hdf1=Hdf.iloc[:,0:1]
Hdf2=Hdf.iloc[:,1:2]
st.write(Hdf1)
st.write(Hdf2)
col_1, col_2 = st.columns([1, 1])
with col_1:
    
    
    

    st.bar_chart(Hdf1,x=Hdf1[index],y=Hdf1[f'{Win1}'])
with col_2:
    
    
    

    st.bar_chart(Hdf2,x=Hdf2[index],y=Hdf2[f'{Win2}'])

