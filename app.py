import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Carregar os dados do CSV
data = pd.read_csv('dados_elemento.csv', sep=',')  # Altere 'seu_arquivo.csv' para o nome do seu arquivo

# Título do aplicativo
st.title('Visualização de Dados de Player')

# Exibir os dados
st.write("Dados Brutos:")
st.dataframe(data)

# Gráfico de barras
st.bar_chart(data['placarA'])

# Filtrar dados
time_selecionado = st.selectbox("Escolha um time:", data['playA'].unique())
dados_filtrados = data[data['playA'] == time_selecionado]

st.write(f"Resultados para {time_selecionado}:")
st.dataframe(dados_filtrados)

# Gráfico de pizza usando Matplotlib
placar_counts = dados_filtrados['placarA'].value_counts()
fig, ax = plt.subplots()
ax.pie(placar_counts, labels=placar_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)

# Gráfico de pizza usando Plotly
placar_counts_plotly = dados_filtrados['placarA'].value_counts().reset_index()
placar_counts_plotly.columns = ['Placar', 'Frequência']

fig_plotly = px.pie(placar_counts_plotly, values='Frequência', names='Placar', title='Distribuição dos Placar')
st.plotly_chart(fig_plotly)
