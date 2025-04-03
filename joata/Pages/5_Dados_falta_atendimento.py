import streamlit as st 
import plotly.express as px
import pandas as pd
import Dashboard

motivo_nao_visita = Dashboard.df_depressao['Motivo_Nao_Visitar_Medico_Depressao'].map(Dashboard.motivo_nao_visitar_map).value_counts().reset_index()
motivo_nao_visita.columns = ['Motivo', 'Quantidade']

# Criar gráfico de pizza para os motivos de não visita ao médico
fig_motivo_nao_visitar = px.pie(motivo_nao_visita, names='Motivo', values='Quantidade', 
                                title="Motivos para Não Visitar o Médico/Serviço de Saúde Regularmente")

# Exibir o gráfico
st.plotly_chart(fig_motivo_nao_visitar)