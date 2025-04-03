import streamlit as st 
import plotly.express as px
import pandas as pd
import Dashboard
# Carrega os dados 

Dashboard.df_depressaO= Dashboard.df[Dashboard.df['Diagnostico_Depressao'] == 1]
total_depressao = Dashboard.df_depressao.shape[0]
media_horas_trabalho = Dashboard.df_depressao['Horas_Trabalho_Semana'].mean()
#Printa  a quantidade  de pessoas na DB 
st.write("Quantidade de pessoas na base de dados que tem o diagnóstico de depressão ")
st.metric(label="Total de Pessoas com Diagnóstico de Depressão", value=total_depressao)

st.write("A média de horas trabalhadas por pessoas com diagnóstico é : ")
st.metric(label="Média de Horas de Trabalho por Semana (Pessoas com Depressão)", value=round(media_horas_trabalho, 2))


st.write("Pessoas por estado do Norte : ")

fig = px.bar(Dashboard.depressao_por_estado, x='Estado', y='Quantidade', text='Quantidade', labels={'Quantidade': 'Número de Pessoas'}, 
             title="Número de Pessoas com Diagnóstico de Depressão por Estado")
fig.update_traces(textposition='outside')

st.plotly_chart(fig)