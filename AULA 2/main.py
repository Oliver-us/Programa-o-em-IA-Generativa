import streamlit as st # Interface Gráfica
import pandas as pd # Tratamento de Dados
from sklearn.linear_model import LinearRegression # Modelo de treinamento


st.header('PREVISÃO DE VENDAS')


# Carregar os dados
dados = pd.read_csv('vendas.csv')

df = pd.DataFrame(dados)


# Mostrar os dados
st.write(df)


# Treinar os dados

X = df[['mes']]
Y = df['vendas']

model = LinearRegression().fit(X, Y)


# Informar o mês que deseja prever

mes = st.number_input(
    'Digite o mês para realizar a previsão:',
    min_value=1,
    max_value=12,
    value=9
)


# Botão para realizar a previsão

if st.button('Analisar'):

    # Previsão

    previsao = model.predict([[mes]])[0]

    # Resultado

    st.write(f'Vendas previstas para o mês {mes}: R$ {previsao:.2f}')