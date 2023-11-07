import streamlit as st
import conv_moedas as c_moed
import conv_bases as bases_num
import conv_temperatura as c_temp
import c as img
import c2 as img2
import dias_vividos as d_vividos
import calculadora as calc_basica


st.set_page_config("RemaKing")

img2.img_fundo_home()
st.sidebar.title('Menu')

paginaselecionada = st.sidebar.selectbox('Selecione a ferramenta que deseja', ['--', 'CALCULADORA', 'CONVERSÃO DE BASES', 'CONVERSÃO DE MOEDAS', 'CONVERSÃO DE TEMPERATURA', 'DIAS VIVIDOS'])

if paginaselecionada == '--':
    st.write('')

elif paginaselecionada == 'CALCULADORA':
    img.img_fundo_pag()
    calc_basica.calculadora()

elif paginaselecionada == 'CONVERSÃO DE BASES':
    img.img_fundo_pag()
    bases_num.bases()

elif paginaselecionada == 'CONVERSÃO DE MOEDAS':
    img.img_fundo_pag()
    c_moed.moedas()

elif paginaselecionada == 'CONVERSÃO DE TEMPERATURA':
    img.img_fundo_pag()
    c_temp.temperatura()

elif paginaselecionada == 'DIAS VIVIDOS':
    img.img_fundo_pag()
    d_vividos.dias_vividoss()
