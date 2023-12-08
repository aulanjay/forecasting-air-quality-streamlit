import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(layout="wide",
                   page_icon=":hotsprings:")
st.markdown("<h1 style='text-align: center;'>HUBUNGAN ANTARA RUANG TERBUKA HIJAU DENGAN PM2.5</h1>", unsafe_allow_html=True)
tab1, tab2 = st.tabs(["Korelasi", "Heatmap"])


# Tab 1
with tab1:
    col1, col2 = st.columns(2)
    # Read dataset 
    df_corr = pd.read_csv("dataset/hasil_korelasi.csv")
    df_heatmap = pd.read_csv("dataset/hasil_korelasi_heatmap.csv")
    df_interval = pd.read_csv("dataset/interval.csv")

    # Menampilkan tabel yang berisi data dari dataset 
    # st.checkbox("Use container width", value=False, key="use_container_width")
    # Kolom 1
    with col1:
        st.subheader("Tabel Korelasi Antar Variabel")
        st.dataframe(df_corr, width=500) #use_container_width=st.session_state.use_container_width)

    # Kolom 2
    with col2:
        st.subheader("Tabel Tingkat Hubungan Korelasi")
        st.dataframe(df_interval, width=500)
    
    def read_markdown_file(mf):
        return Path(mf).read_text()
    korelasi = read_markdown_file("markdown/korelasi.md")
    st.markdown(korelasi, unsafe_allow_html=True)

# Tab 2
with tab2:
    st.markdown("<h1 style='text-align: center;'>KORELASI DALAM BENTUK HEATMAP</h1>", unsafe_allow_html=True)
    # Mengganti nama pada sumbu Y
    yticklabels = df_heatmap.columns
    yticklabels = ['Year', 'PM2.5', 'RTH']

    # Menampilkan korelasi dengan menggunakan heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(df_heatmap, annot=True, cmap="coolwarm", yticklabels=yticklabels)
    plt.title("Heatmap Korelasi Antara Year vs PM 2.5 vs RTH")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot() 