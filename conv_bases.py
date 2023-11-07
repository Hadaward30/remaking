import streamlit as st

def bases():

    st.title('Conversor de bases númericas')
    input_opcao = st.selectbox('De:', ['BINÁRIO', 'DECIMAL', 'HEXADECIMAL', 'OCTAL'])
    output_opcao = st.selectbox('Para:', ['BINÁRIO', 'DECIMAL', 'HEXADECIMAL', 'OCTAL'])

    if input_opcao == output_opcao:
        st.write("Bases númericas iguais. Nenhuma conversão necessária.")
    if input_opcao == 'DECIMAL':
        if output_opcao == 'BINÁRIO':
            base_number = st.number_input('Informe o número que deseja converter', 0)
            if st.button('CONVERTER'):
                st.success(bin(base_number)[2:])

        elif output_opcao == 'HEXADECIMAL':
            base_number = st.number_input('Informe o número que deseja converter', 0)
            if st.button('CONVERTER'):
                st.success(hex(base_number)[2:].upper())

        elif output_opcao == 'OCTAL':
            base_number = st.number_input('Informe o número que deseja converter', 0)
            if st.button('CONVERTER'):
                st.success(oct(base_number)[2:])

    elif input_opcao == 'BINÁRIO':
        if output_opcao == 'DECIMAL':
            base_number = st.number_input('Informe o número que deseja converter', 0)
            n = len(str(base_number))
            valor_digitado = base_number
            decimal = 0
            i = 0
            while n >= 0:
                resto = base_number % 10
                decimal = decimal + (resto * (2 ** i))
                n = n - 1
                i = i + 1
                base_number = base_number // 10
            if st.button('CONVERTER'):
                st.success(decimal)

        elif output_opcao == 'HEXADECIMAL':
            base_number = st.number_input('Informe o número que deseja converter', 0)
            n = len(str(base_number))
            valor_digitado = base_number
            decimal = 0
            i = 0
            while n >= 0:
                resto = base_number % 10
                decimal = decimal + (resto * (2 ** i))
                n = n - 1
                i = i + 1
                base_number = base_number // 10
            if st.button('CONVERTER'):
                st.success(hex(decimal)[2:].upper())

        elif output_opcao == 'OCTAL':
            base_number = st.number_input('Informe o número que deseja converter', 0)
            n = len(str(base_number))
            valor_digitado = base_number
            decimal = 0
            i = 0
            while n >= 0:
                resto = base_number % 10
                decimal = decimal + (resto * (2 ** i))
                n = n - 1
                i = i + 1
                base_number = base_number // 10
            if st.button('CONVERTER'):
                st.success(oct(decimal)[2:])

    elif input_opcao == 'HEXADECIMAL':
        if output_opcao == 'BINÁRIO':
            base_number = st.text_input('Informe o número que deseja converter', 0)
            decimal = int(base_number, 16)
            binario = bin(decimal)
            if st.button('CONVERTER'):
                st.success(binario[2:])
        if output_opcao == 'DECIMAL':
            base_number = st.text_input('Informe o número que deseja converter', 0)
            decimal = int(base_number, 16)
            if st.button('CONVERTER'):
                st.success(decimal)
        if output_opcao == 'OCTAL':
            base_number = st.text_input('Informe o número que deseja converter', 0)
            decimal = int(base_number, 16)
            octal = oct(decimal)
            if st.button('CONVERTER'):
                st.success(octal[2:])

    else:
        if output_opcao == 'BINÁRIO':
            base_number = st.text_input('Informe o número que deseja converter', 0)
            decimal = int(base_number, 8)
            binario = bin(decimal)
            if st.button('CONVERTER'):
                st.success(binario[2:])

        elif output_opcao == 'DECIMAL':
            base_number = st.text_input('Informe o número que deseja converter', 0)
            decimal = int(base_number, 8)
            if st.button('CONVERTER'):
                st.success(decimal)
        elif output_opcao == 'HEXADECIMAL':
            base_number = st.text_input('Informe o número que deseja converter', 0)
            decimal = int(base_number, 8)
            binario = hex(decimal)
            if st.button('CONVERTER'):
                st.success(binario[2:].upper())
