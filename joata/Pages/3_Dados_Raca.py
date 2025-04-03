import streamlit as st 
import plotly.express as px
import pandas as pd
import Dashboard

fig_raca = px.bar(Dashboard.depressao_por_raca, x='Raça', y='Quantidade', text='Quantidade', 
                  labels={'Quantidade': 'Número de Pessoas'}, title="Número de Pessoas com Diagnóstico de Depressão por Raça")
fig_raca.update_traces(textposition='outside')

st.plotly_chart(fig_raca)
