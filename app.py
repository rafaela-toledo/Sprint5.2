import streamlit as st
import pandas as pd
import plotly.express as px

data_car = pd.read_csv("vehicles.csv")

# Botão para criar um histograma
hist_button = st.button('Criar histograma') 
if hist_button: 
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig_hist = px.histogram(data_car, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Botão para criar um gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão') 
if scatter_button: 
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig_scatter = px.scatter(data_car, x="odometer", y="price", title="Relação entre Quilometragem e Preço",
                             labels={"odometer": "Quilometragem", "price": "Preço"})
    st.plotly_chart(fig_scatter, use_container_width=True)
