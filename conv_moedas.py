import requests
import json
import streamlit as st

def moedas():
    cotacao = requests.get("https://economia.awesomeapi.com.br/json/last/EUR-USD,USD-BRL,USD-EUR,BRL-USD,BRL-EUR,EUR-BRL")
    cotacoes = cotacao.json()

    st.title('Conversor de Moedas')
    input_opcao = st.selectbox('De:', ['USD', 'EUR', 'BRL'])
    output_opcao = st.selectbox('Para:', ['USD', 'EUR', 'BRL'])

    if input_opcao == output_opcao:
        st.write("As moedas inseridas são iguais. Nenhuma conversão necessária.")

    if input_opcao == 'USD':
        if output_opcao == 'BRL':
            valor = st.number_input('Informe o valor desejado', 0.0)
            dolar = float(cotacoes["USDBRL"]["bid"])
            resultado = dolar * valor

            if st.button('CONVERTER'):
                st.success("$$ {:.2f} É equivalente a R$ {:.2f}".format(valor, resultado))

        elif output_opcao == 'EUR':
            valor = st.number_input('Informe o valor desejado', 0.0)
            dolar_euro = float(cotacoes['USDEUR']['bid'])
            resultado = dolar_euro * valor

            if st.button('CONVERTER'):
                st.success("$$ {:.2f} É equivalente a € {:.2f}".format(valor, resultado ))

    elif input_opcao == 'BRL':
        if output_opcao == 'USD':
            real_dolar = (float(cotacoes['BRLUSD']['bid']))
            valor2 = st.number_input('Informe o valor desejado', 0.0)
            resultado2 = real_dolar * valor2

            if st.button('CONVERTER'):
                st.success('R$ {:.2f} É equivalente a $$ {:.2f}'.format(valor2, resultado2))

        elif output_opcao == 'EUR':
            valor2 = st.number_input('Informe o valor desejado', 0.0)
            real_euro = (float(cotacoes['BRLEUR']['bid']))
            resultado2 = real_euro * valor2

            if st.button('CONVERTER'):
                st.success('R$ {:.2f} É equivalente a € {:.2f}'.format(valor2, resultado2))

    elif input_opcao == 'EUR':
        if output_opcao == 'BRL':
            valor2 = st.number_input('Informe o valor desejado', 0.0)
            euro_real = (float(cotacoes['EURBRL']['bid']))
            resultado2 = euro_real * valor2

            if st.button('CONVERTER'):
                st.success('€ {:.2f} É equivalente a R$ {:.2f}'.format(valor2, resultado2))

        elif output_opcao == 'USD':
            valor2 = st.number_input('Informe o valor desejado', 0.0)
            euro_dol = (float(cotacoes['EURUSD']['bid']))
            resultado2 = euro_dol * valor2

            if st.button('CONVERTER'):
                st.success('€ {:.2f} É equivalente a $$ {:.2f}'.format(valor2, resultado2))
