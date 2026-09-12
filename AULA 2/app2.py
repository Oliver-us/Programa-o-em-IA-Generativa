from sklearn.tree import DecisionTreeClassifier
import numpy as np
import streamlit as st

#tempo de uso de produto X numero de reclamações

X = np.array([
    [1,1],
    [5,4],
    [3,3],
    [4,1],
    [4,1],
    [5,0]
])

#0 -> fica - 1 -> cancela

Y = np.array([0,1,1,0,1,1])

modelo = DecisionTreeClassifier()
modelo.fit(X,Y)

uso = st.number_input('Quantidade de vezes que o produto foi utilizado: ', value = 0)
reclamacoes = st.number_input('Reclamações: ', value = 0)

st.header('Analise de cancelamentos')

if st.button('analisar cliente'):
    if modelo.predict([[uso, reclamacoes]]) == 0:
        st.write('CLIENTE CONSOLIDADO')
    else:
        st.write('POSSÌVEL CANCELAMENTO')

print(modelo.predict([[5,2]]))
print(modelo.predict([[5,2]]))
print(modelo.predict([[5,2]]))
print(modelo.predict([[5,2]]))
print(modelo.predict([[5,2]]))