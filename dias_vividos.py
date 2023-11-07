import streamlit as st
from datetime import datetime

def dias_vividoss():

    st.title("Calculadora de Dias Vividos")

    dia_nascimento = st.number_input("Dia de Nascimento:", min_value=1, max_value=31)
    mes_nascimento = st.number_input("Mês de Nascimento:", min_value=1, max_value=12)
    ano_nascimento = st.number_input("Ano de Nascimento:", min_value=1)

    if st.button("Calcular"):
        data_nascimento = datetime(ano_nascimento, mes_nascimento, dia_nascimento)
        data_atual = datetime.now()
        dias_vividos = (data_atual - data_nascimento).days
        st.success(f"Você viveu {dias_vividos} dias até hoje.")
