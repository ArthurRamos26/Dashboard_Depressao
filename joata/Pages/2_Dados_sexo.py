import streamlit as st 
import plotly.express as px
import pandas as pd
import Dashboard

fig_sexo = px.pie(Dashboard.depressao_por_sexo, names='Sexo', values='Quantidade', title="Comparação de Homens e Mulheres com Diagnóstico de Depressão")
st.plotly_chart(fig_sexo)
