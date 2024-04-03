import streamlit as st
import pandas as pd
import plotly.express as px

data_car = pd.read_csv("vehicles.csv")
hist_button = st.button('Criar histograma') 
     
if hist_button: 
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(data_car, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão') 

if scatter_button: 
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig_scatter = px.scatter(data_car, x="x_coluna", y="y_coluna")
    st.plotly_chart(fig_scatter, use_container_width=True)