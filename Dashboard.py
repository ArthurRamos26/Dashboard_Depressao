import streamlit as st
import pandas as pd
import plotly.express as px

# Caminho do arquivo de dados
caminho_arquivo = r"C:\Users\Aluno\Desktop\trabalho final\pns2019_dashboard_renomeado_IA (1).csv"

# Carregar os dados
df = pd.read_csv(caminho_arquivo, sep=';', encoding='utf-8')

# Dicionário de estados
estados = {
    11: 'Rondônia', 
    12: 'Acre',
    13: 'Amazonas',
    14: 'Roraima',
    15: 'Pará',
    16: 'Amapá',
    17: 'Tocantins'
}

# Map de estado civil
estado_civil_map = {
    1: 'Casado(a)',
    2: 'Divorciado(a) ou desquitado(a) ou separado(a) judicialmente',
    3: 'Viúvo(a)',
    4: 'Solteiro(a)',
}

# Map de avaliação estado físico/mental
avaliacao_map = {
    1: 'Muito boa',
    2: 'Boa',
    3: 'Regular',
    4: 'Ruim',
    5: 'Muito ruim'
}

# Map de raças para um formato legível
raca_map = {
    1: 'Branca',
    2: 'Preta',
    3: 'Parda',
    4: 'Amarela',
    5: 'Indígena',
}

# Map motivos para não visitar o médico
motivo_nao_visitar_map = {
    1: 'Não está mais deprimido',
    2: 'O serviço de saúde é distante ou tem dificuldade de transporte',
    3: 'Não tem ânimo',
    4: 'O tempo de espera no serviço de saúde é muito grande',
    5: 'Tem dificuldades financeiras',
    6: 'O horário de funcionamento do serviço de saúde é incompatível com suas atividades de trabalho ou domésticas',
    7: 'Não conseguiu marcar consulta pelo plano de saúde',
    8: 'Não sabe quem procurar ou aonde ir',
    9: 'Outro'
}

# Filtrar apenas as pessoas com diagnóstico de depressão
df_depressao = df[df['Diagnostico_Depressao'] == 1]
total_depressao = df_depressao.shape[0]

# Calcular a média de horas de trabalho das pessoas com depressão
media_horas_trabalho = df_depressao['Horas_Trabalho_Semana'].mean()

#---------------------------------------------------------------------------------------------------------#

# Contar número de pessoas com depressão por estado
depressao_por_estado = df_depressao['Unidade_Federacao'].map(estados).value_counts().reset_index()
depressao_por_estado.columns = ['Estado', 'Quantidade']

#---------------------------------------------------------------------------------------------------------#

# Filtrar valores válidos para a coluna 'Avaliacao_Estado_Saude_BemEstar'
df_estado_saude = df[df['Avaliacao_Estado_Saude_BemEstar'].isin([1, 2, 3, 4, 5])]

# Contar a quantidade de pessoas em cada categoria de avaliação
avaliacao_estado_saude = df_estado_saude['Avaliacao_Estado_Saude_BemEstar'].value_counts().reset_index()
avaliacao_estado_saude.columns = ['Avaliacao', 'Quantidade']

# Mapear os valores de avaliação para um formato legível
avaliacao_estado_saude['Avaliacao'] = avaliacao_estado_saude['Avaliacao'].map(avaliacao_map)

#---------------------------------------------------------------------------------------------------------#

# Contar o número de pessoas com depressão por estado civil
depressao_por_estado_civil = df_depressao['Estado_Civil'].map(estado_civil_map).value_counts().reset_index()
depressao_por_estado_civil.columns = ['Estado Civil', 'Quantidade']

#---------------------------------------------------------------------------------------------------------#

# Contar o número de pessoas com depressão por raça
depressao_por_raca = df_depressao['Cor_Raca'].value_counts().reset_index()
depressao_por_raca.columns = ['Raça', 'Quantidade']

depressao_por_raca['Raça'] = depressao_por_raca['Raça'].map(raca_map)

#---------------------------------------------------------------------------------------------------------#

# Contar o número de pessoas com depressão por sexo
depressao_por_sexo = df_depressao['Sexo'].value_counts().reset_index()
depressao_por_sexo.columns = ['Sexo', 'Quantidade']
depressao_por_sexo['Sexo'] = depressao_por_sexo['Sexo'].map({1: 'Masculino', 2: 'Feminino'})

#---------------------------------------------------------------------------------------------------------#
st.image("LOGO_DS.jpg") 

# Criar o dashboard com Streamlit
st.title("Dashboard sobre Depressão")

# Introdução
st.write("""
A depressão é um transtorno mental influenciado por fatores sociais e econômicos. 
         Este dashboard apresenta dados que evidenciam a relação entre esses fatores e a prevalência da depressão, buscando apresentar a relação e impacto desses 
         fatores de forma facilmente visível e clara.
""")

#---------------------------------------------------------------------------------------------------------#

# Exibir o número total de pessoas com depressão
st.metric(label="Total de Pessoas com Diagnóstico de Depressão", value=total_depressao)

#---------------------------------------------------------------------------------------------------------#

# Exibir a média de horas de trabalho de pessoas com depressão
st.metric(label="Média de Horas de Trabalho por Semana (Pessoas com Depressão)", value=round(media_horas_trabalho, 2))

#---------------------------------------------------------------------------------------------------------#

# Criar gráfico de barras com a quantidade de pessoas com depressão por estado
fig = px.bar(depressao_por_estado, x='Estado', y='Quantidade', text='Quantidade', labels={'Quantidade': 'Número de Pessoas'}, 
             title="Número de Pessoas com Diagnóstico de Depressão por Estado")
fig.update_traces(textposition='outside')

st.plotly_chart(fig)

#---------------------------------------------------------------------------------------------------------#

# Criar gráfico de funil para avaliação do estado de saúde
fig_funnel = px.funnel(avaliacao_estado_saude, x='Quantidade', y='Avaliacao', 
                       title="Avaliação do Estado de Saúde (Bem-Estar)")

st.plotly_chart(fig_funnel)

#---------------------------------------------------------------------------------------------------------#

# Criar gráfico de barras com a quantidade de pessoas com depressão por estado civil
fig_estado_civil = px.bar(depressao_por_estado_civil, x='Estado Civil', y='Quantidade', text='Quantidade', 
                          labels={'Quantidade': 'Número de Pessoas'}, title="Número de Pessoas com Diagnóstico de Depressão por Estado Civil")
fig_estado_civil.update_traces(textposition='outside')

st.plotly_chart(fig_estado_civil)

#---------------------------------------------------------------------------------------------------------#

# Criar gráfico de barras com a quantidade de pessoas com depressão por raça
fig_raca = px.bar(depressao_por_raca, x='Raça', y='Quantidade', text='Quantidade', 
                  labels={'Quantidade': 'Número de Pessoas'}, title="Número de Pessoas com Diagnóstico de Depressão por Raça")
fig_raca.update_traces(textposition='outside')

st.plotly_chart(fig_raca)

#---------------------------------------------------------------------------------------------------------#

# Criar gráfico de pizza comparando quantidade de homens e mulheres com depressão
fig_sexo = px.pie(depressao_por_sexo, names='Sexo', values='Quantidade', title="Comparação de Homens e Mulheres com Diagnóstico de Depressão")
st.plotly_chart(fig_sexo)

# Contar o número de pessoas diagnosticadas com depressão que tomam ou não remédio
depressao_com_remedio = df_depressao['Medicamento_Depressao'].map({2: 'Não', 3: 'Não sabe/não respondeu'}).value_counts().reset_index()
depressao_com_remedio.columns = ['Resposta', 'Quantidade']

#---------------------------------------------------------------------------------------------------------#

# Contar o número de pessoas diagnosticadas com depressão que tomam ou não remédio
depressao_com_remedio = df_depressao['Medicamento_Depressao'].map({2: 'Não', 1: 'Sim'}).value_counts().reset_index()
depressao_com_remedio.columns = ['Resposta', 'Quantidade']

# Criar gráfico de pizza para comparar pessoas que tomam ou não remédio
fig_remedio_pizza = px.pie(depressao_com_remedio, names='Resposta', values='Quantidade', 
                           title="Número de Pessoas com Depressão que Tomam ou Não Remédio")

# Exibir o gráfico
st.plotly_chart(fig_remedio_pizza)

#---------------------------------------------------------------------------------------------------------#

# Filtrar a coluna de motivo de não visita
motivo_nao_visita = df_depressao['Motivo_Nao_Visitar_Medico_Depressao'].map(motivo_nao_visitar_map).value_counts().reset_index()
motivo_nao_visita.columns = ['Motivo', 'Quantidade']

# Criar gráfico de pizza para os motivos de não visita ao médico
fig_motivo_nao_visitar = px.pie(motivo_nao_visita, names='Motivo', values='Quantidade', 
                                title="Motivos para Não Visitar o Médico/Serviço de Saúde Regularmente")

# Exibir o gráfico
st.plotly_chart(fig_motivo_nao_visitar)