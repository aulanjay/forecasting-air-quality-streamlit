import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Beranda",
    page_icon="👋",
    layout="wide",
)

st.markdown("<h1 style='text-align: center;'>Aplikasi Prediksi Tingkat Polusi Udara DKI Jakarta</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Selayang Pandang Aplikasi</h2>", unsafe_allow_html=True)

def read_markdown_file(markdown_file):
        return Path(markdown_file).read_text()
intro_markdown = read_markdown_file("markdown/apk.md")
st.markdown(intro_markdown, unsafe_allow_html=True)
st.write("---")

st.sidebar.success("Pilih halaman di atas.")
st.subheader("Pendahuluan :wave:")
        
intro_markdown = read_markdown_file("markdown/pendahuluan.md")
st.markdown(intro_markdown, unsafe_allow_html=True)
        
st.write("---")