import streamlit as st

def img_fundo_pag():
    page_bg_imge = f"""
                <style>
            [data-testid ="stAppViewContainer"] {{
            background-image: url(https://a.imagem.app/batHpt.png);
            background-size: cover;
            font-size: 16px;
             }}


            </style>
            """
    st.markdown(page_bg_imge, unsafe_allow_html=True)

