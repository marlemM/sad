import streamlit as st
import pandas as pd

# Carregar os dados do CSV
data = pd.read_csv('dados_elemento.csv', sep=',')  # Altere 'seu_arquivo.csv' para o nome do seu arquivo

# Título do aplicativo
st.title('Visualização de Dados de Player')

# Exibir os dados
st.write("Dados Brutos:")
st.dataframe(data)

# Gráfico simples
st.bar_chart(data['placarA'])

# Filtrar dados
time_selecionado = st.selectbox("Escolha um time:", data['playA'].unique())
dados_filtrados = data[data['playA'] == time_selecionado]

st.write(f"Resultados para {time_selecionado}:")
st.dataframe(dados_filtrados)
