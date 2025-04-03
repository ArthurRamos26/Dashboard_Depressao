import streamlit as st 

st.set_page_config (
    page_title="Dashboard Depressão",
    page_icon="LOGO_DS.jpg"
)
st.sidebar.success("Páginas")
# Criar o dashboard com Streamlit
st.title("Dashboard sobre Depressão")

# Introdução
st.write("""
A depressão é um transtorno mental influenciado por fatores sociais e econômicos. 
         Este dashboard apresenta dados que evidenciam a relação entre esses fatores e a prevalência da depressão, buscando apresentar a relação e impacto desses 
         fatores de forma facilmente visível e clara.
""")
 