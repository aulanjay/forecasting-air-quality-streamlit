import streamlit as st
import pandas as pd
from PIL import Image
from pathlib import Path

st.set_page_config(layout="wide",
                   page_icon=":earth_asia:",
                   page_title="Kluster PM2.5 DKI Jakarta")

st.markdown("<h1 style='text-align: center;'>ANALISIS KLUSTER LUASAN WILAYAH RTH DKI JAKARTA TAHUN 2022</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Clustering</h1>", unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    image = Image.open('image/clusterz.jpeg')
    st.image(image, width=600)

    legenda = Image.open('image/cluster1.jpeg')
    st.image(legenda,width=585)

with col2:
    st.subheader("Cluster 1")
    st.markdown("""
                Wilayah yang termasuk Cluster 1 ialah yang memiliki Ruang Terbuka Hijau paling rendah. Yaitu di rentang 0,02 - 0,83 m.
                
                Wilayah yang termasuk Cluster 1 adalah :
                1. Jakarta Pusat
                2. Jakarta Barat
                3. Jakarta Utara
                4. Jakarta Timur
            """)
    st.subheader("Cluster 2")
    st.markdown("Wilayah yang termasuk Cluster 2 ialah yang memiliki Ruang Terbuka Hijau paling luas dengan rata - rata luasnya mencapai 326,88 m. Wilayah yang termasuk Cluster 2 adalah Jakarta Selatan")

    st.subheader("Cluster 3")
    st.markdown("Wilayah yang termasuk Cluster 3 ialah yang memiliki Ruang Terbuka Hijau dengan rata - rata luas mencapai 290.63 m. Wilayah yang termasuk Cluster 3 adalah Kepulauan Seribu")

    df = pd.read_csv('dataset/kluster.csv')
    st.table(df)

with st.expander("Lihat Penjelasan"):
        def read_markdown_file(mf):
            return Path(mf).read_text()
     
        clust = read_markdown_file("markdown/cluster.md")
        st.markdown(clust, unsafe_allow_html=True)
