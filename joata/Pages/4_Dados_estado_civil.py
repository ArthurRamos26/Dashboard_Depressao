import streamlit as st 
import plotly.express  as px  
import pandas as pd
import Dashboard


depressao_por_estado_civil = Dashboard.df_depressao['Estado_Civil'].map(Dashboard.estado_civil_map).value_counts().reset_index()

depressao_por_estado_civil.columns = ['Estado Civil', 'Quantidade']

fig_estado_civil = px.bar(depressao_por_estado_civil, x='Estado Civil', y='Quantidade', text='Quantidade', 
                         
                          labels={'Quantidade': 'Número de Pessoas'}, title="Número de Pessoas com Diagnóstico de Depressão por Estado Civil")

fig_estado_civil.update_traces(textposition='outside')

st.plotly_chart(fig_estado_civil)