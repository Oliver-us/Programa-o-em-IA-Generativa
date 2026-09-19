import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Configuração inicial da página
st.set_page_config(
    page_title="IA da Energia do Café",
    page_icon="☕",
    layout="centered"
)

# Título e Apresentação
st.title("☕ IA da Energia do Café")
st.subheader("Aplicação de Regressão Linear para Iniciantes")
st.write("Bem-vindo(a)! Esta aplicação utiliza Machine Learning para prever o seu **nível de energia** com base no consumo de **xícaras de café**.")

st.markdown("---")

# 1. Preparação dos Dados (Exatamente conforme os requisitos)
cafe = pd.DataFrame({
    'xicaras': [1, 2, 3, 4, 5],
    'energia': [2, 4, 6, 8, 10]
})

# Exibição dos dados de treino
with st.expander("📊 Visualizar Dados de Treinamento"):
    st.write("O modelo foi treinado com os seguintes dados:")
    st.dataframe(cafe)

# 2. Treinamento do Modelo de Regressão Linear
# Definindo variável de entrada (X) e variável alvo (y)
X = cafe[['xicaras']] # Entradas (Features)
y = cafe['energia']   # Alvo (Target)

modelo = LinearRegression()
modelo.fit(X, y)

st.markdown("---")

# 3. Interação com o Usuário
st.header("🔮 Faça sua Previsão")

xicara_input = st.number_input(
    label="Informe a quantidade de xícaras de café consumidas:",
    min_value=0.0,
    max_value=20.0,
    value=1.0,
    step=0.5
)

# Botão para realizar a previsão
if st.button("Prever Nível de Energia ⚡"):
    # Realizando a predição com o modelo treinado
    previsao = modelo.predict([[xicara_input]])[0]
    
    # Exibição do Resultado
    st.success(f"Nível de energia estimado: **{previsao:.2f}**")

st.markdown("---")

# 4. Explicação Didática do Modelo
st.header("🧠 Como o modelo realizou esta previsão?")

st.write(
    """
    A **Regressão Linear** busca encontrar uma relação matemática em linha reta entre a variável de entrada (xícaras de café) e a variável de saída (nível de energia).
    
    A fórmula da linha reta é representada por:
    $$Energia = (Coeficiente \\times Xícaras) + Intercepto$$
    """
)

# Recuperando parâmetros aprendidos pelo modelo
coeficiente = modelo.coef_[0]
intercepto = modelo.intercept_

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Coeficiente (Peso por xícara)", value=f"{coeficiente:.2f}")
with col2:
    st.metric(label="Intercepto (Energia base)", value=f"{intercepto:.2f}")

st.info(
    f"Neste modelo, cada xícara de café aumenta o nível de energia em **{coeficiente:.1f}** unidades. "
    f"Portanto, para **{xicara_input}** xícara(s), o cálculo é: "
    f"({coeficiente:.1f} × {xicara_input}) + {intercepto:.1f} = **{coeficiente * xicara_input + intercepto:.1f}**."
)

st.markdown("---")

# Rodapé informativo
st.caption("⚠️ **Nota Didática:** Os dados utilizados nesta aplicação são fictícios e foram elaborados exclusivamente para fins acadêmicos e pedagógicos no curso técnico de Desenvolvimento de Sistemas.")