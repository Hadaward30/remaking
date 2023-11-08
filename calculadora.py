import streamlit as st

def calculadora():

    st.title('Calculadora')
    operacao = st.selectbox("Selecione a operação", ("Soma", "Subtração", "Multiplicação", "Divisão", "Raiz quadrada"))

    if operacao == 'Raiz quadrada':
        num1 = st.number_input('Informe o número que deseja descobrir a raiz quadrada', 0)
        if st.button("CALCULAR"):
            st.success('A raiz quadrada de {} é {:.2f}'.format(num1, num1 ** (1 / 2)))

    elif operacao == 'Soma':
        num1 = st.number_input("Insira o primeiro número")
        num2 = st.number_input("Insira o segundo número")
        resultado = num1 + num2
        if st.button("CALCULAR"):
            st.success('{:.2f} + {:.2f} = {:.2f}'.format(num1, num2, resultado))

    elif operacao == 'Subtração':
        num1 = st.number_input("Insira o primeiro número")
        num2 = st.number_input("Insira o segundo número")
        resultado = num1 - num2
        if st.button("CALCULAR"):
            st.success('{:.2f} - {:.2f} = {:.2f}'.format(num1, num2, resultado))

    elif operacao == 'Multiplicação':
        num1 = st.number_input("Insira o primeiro número")
        num2 = st.number_input("Insira o segundo número")
        resultado = num1 * num2
        if st.button("CALCULAR"):
            st.success('{:.2f} * {:.2f} = {:.2f}'.format(num1, num2, resultado))

    elif operacao == 'Divisão':
        num1 = st.number_input("Insira o primeiro número")
        num2 = st.number_input("Insira o segundo número")
        if num2 != 0:
            resultado = num1 / num2
        else:
            st.error("Divisão por zero não é permitida")

        if st.button("CALCULAR"):
            st.success('{:.2f} ÷ {:.2f} = {:.2f}'.format(num1, num2, resultado))

