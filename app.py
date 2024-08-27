#importação dos pacotes

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression


#Carregando base de dados

db = pd.read_csv('pizzas.csv')


#Treinando modelo

modelo = LinearRegression()
x = db[["diametro"]]
y = db[["preco"]]


#Criando interface web

st.title("Prevendo o valor de uma pizza")
st.divider()

diametro = st.number_input("Digite o diametro da pizza: ")
preco_previsto = 'Olá, mundo'

if (diametro > 0):
    preco_previsto = modelo.predict([[diametro]][0][0])
    st.write(f"O valor da pizza com diamentro {diametro} é de R$ {preco_previsto}")
else:
    st.write("Por favor, digite um valor válido")