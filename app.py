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