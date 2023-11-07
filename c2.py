import streamlit as st

def img_fundo_home():
    page_bg_img = f"""

    <style>
    [data-testid ="stAppViewContainer"] {{
    background-image: url("https://a.imagem.app/bU1DmS.png");
    background-size: cover;
    font-size: 16px;
     }}

    [data-testid="stSidebar"] {{
    background-color: rgba(35,30,63,0.5);
    }}
    [data-testid="stHeader"] {{
    background-color: rgba(30,57,63,0.0);
    }}
    [data-testid="stDecoration"] {{
    height: 0rem;
    }}
    footer {{
    visibility: hidden;
    }}
"""

    st.markdown(page_bg_img, unsafe_allow_html=True)