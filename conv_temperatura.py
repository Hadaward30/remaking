import streamlit as st

def temperatura():

    st.title("Conversor de Temperatura")

    input_opcao = st.selectbox("De:", ("Celsius", "Fahrenheit", "Kelvin"))
    output_opcao = st.selectbox("Para:", ("Celsius", "Fahrenheit", "Kelvin"))

    if input_opcao == output_opcao:
        st.write("A temperatura de entrada e a escala de saída são iguais. Nenhuma conversão necessária.")
    if input_opcao == "Celsius":
        if output_opcao == "Fahrenheit":
            temperatura = st.number_input("Digite a temperatura a ser convertida:")

            resultado = (temperatura * 9 / 5) + 32
            if st.button('CONVERTER'):
                st.success(f"{temperatura} graus {input_opcao} são equivalentes a {resultado:.2f} graus {output_opcao}.")

        elif output_opcao == "Kelvin":
            temperatura = st.number_input("Digite a temperatura a ser convertida:")
            resultado = temperatura + 273.15
            if st.button('CONVERTER'):
                st.success(f"{temperatura} graus {input_opcao} são equivalentes a {resultado:.2f} graus {output_opcao}.")

    elif input_opcao == "Fahrenheit":
        if output_opcao == "Celsius":
            temperatura = st.number_input("Digite a temperatura a ser convertida:")
            resultado = (temperatura - 32) * 5 / 9
            if st.button('CONVERTER'):
                st.success(f"{temperatura} graus {input_opcao} são equivalentes a {resultado:.2f} graus {output_opcao}.")

        elif output_opcao == "Kelvin":
            temperatura = st.number_input("Digite a temperatura a ser convertida:")
            resultado = ((temperatura - 32) * 5 / 9) + 273.15
            if st.button('CONVERTER'):
                 st.success(f"{temperatura} graus {input_opcao} são equivalentes a {resultado:.2f} graus {output_opcao}.")

    elif input_opcao == "Kelvin":
        if output_opcao == "Celsius":
            temperatura = st.number_input("Digite a temperatura a ser convertida:")
            resultado = temperatura - 273.15
            if st.button('CONVERTER'):
                st.success(f"{temperatura} graus {input_opcao} são equivalentes a {resultado:.2f} graus {output_opcao}.")

        elif output_opcao == "Fahrenheit":
            temperatura = st.number_input("Digite a temperatura a ser convertida:")
            resultado = ((temperatura - 273.15) * 9 / 5) + 32
            if st.button('CONVERTER'):
                st.success(f"{temperatura} graus {input_opcao} são equivalentes a {resultado:.2f} graus {output_opcao}.")


