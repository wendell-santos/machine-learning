import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Carregando base de dados
db = pd.read_csv('pizzas.csv')

# Treinando modelo
modelo = LinearRegression()
x = db[["diametro"]]
y = db[["preco"]]
modelo.fit(x, y)

# Criando interface web
st.title("Prevendo o valor de uma pizza")
st.divider()

diametro = st.number_input("Digite o diametro da pizza: ")

if diametro > 0:
    preco_previsto = modelo.predict([[diametro]])[0][0]  # Correção aqui
    st.write(f"O valor da pizza com diâmetro {diametro} é de R$ {preco_previsto:.2f}.")
