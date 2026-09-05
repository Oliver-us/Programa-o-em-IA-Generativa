import streamlit as st

st.title("Cadastro de Usuário")

nome = st.text_input("Nome")

idade = st.number_input(
    "Idade",
    min_value=0,
    max_value=120
)

aceitou_termos = st.checkbox("Aceito os termos de uso")

if st.button("Cadastrar"):

    if nome == "":
        st.warning("Digite seu nome.")

    elif not aceitou_termos:
        st.warning("Você precisa aceitar os termos de uso.")

    else:
        st.success("Cadastro realizado com sucesso!")

        st.write("Nome:", nome)
        st.write("Idade:", idade)
        st.write("Aceitou os termos:", aceitou_termos)