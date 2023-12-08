import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(layout="wide",
                   page_icon=":loudspeaker:")
tab1, tab2, tab3= st.tabs(["PM2.5 Emission In Jakarta", "Statistik Deskriptif", "Informasi Tingkat PM2.5"])


# Tab 1
with tab1:
    st.title("PM2.5 AIR POLUTION")

    st.header("SOURCE")
    st.markdown("Particulate Matter (PM2.5) adalah partikel udara yang berukuran lebih kecil dari atau sama dengan 2.5µm (mikrometer). Dari semua tindakan polusi udara, PM2.5 merupakan ancaman kesehatan terbesar. Karena ukurannya yang kecil, PM2.5 dapat tetap melayang di udara untuk waktu yang lama dan dapat diserap jauh ke dalam aliran darah saat terhirup.")

    st.header("PM2.5 EMISSION IN JAKARTA")

    # Membaca Dataset
    df = pd.read_csv('dataset/Mean_PM25 pertahun.csv')

    # Tambahkan checkbox untuk setiap tahun
    selected_years = st.multiselect('Pilih Tahun', df['year'].unique())

    # Filter dataset berdasarkan tahun yang dipilih
    filtered_data = df[df['year'].isin(selected_years)]

    # Tampilkan grafik PM2.5 per tahun berdasarkan checkbox
    if not filtered_data.empty:
        st.write('### Grafik PM2.5 per Tahun')
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='year', y='pm25', data=filtered_data, marker='o')
        plt.xlabel('Tahun')
        plt.ylabel('PM2.5')
        plt.title('Grafik PM2.5 per Tahun')
        st.pyplot()
    else:
        st.warning('Data untuk tahun yang dipilih tidak tersedia.')
        st.set_option('deprecation.showPyplotGlobalUse', False)

# Tab 2
# Menghitung Nilai PM2.5
with tab2:
    average_pm25 = df['pm25'].mean()
    min_pm25 = df['pm25'].min()
    max_pm25 = df['pm25'].max()
    deviasi = 19.2

    # Tampilkan hasil dalam bentuk tabel
    st.write('### Statistik Deskriptif')
    st.table({
        'Informasi' : ['Standar Deviasi', 'Rata-Rata', 'Nilai Minimum', 'Nilai Maximum'],
        'Tingkatan PM2.5' : [deviasi, average_pm25, min_pm25, max_pm25],
    })

    with st.expander("Lihat Penjelasan"):
        st.markdown("""
        <div style="text-align: left;">
                    <h3>Statistika Deskriptif</h3>
                    <p>Statisika Deskriptif meliputi nilai rata-rata (mean), median, modus, deviasi standar, kuartil, rentang, dan sebagainya. Statistik ini membantu memberikan gambaran umum tentang distribusi data. Kali ini akan dianalisis mengenai variabel pm2.5 dan pm10 yang digunakan.</p>
                    <p>Exploratory Data Analysis. Ini adalah proses dalam analisis data yang bertujuan untuk menjelajahi dan memahami struktur, pola, serta karakteristik dari data yang tersedia. Data yang digunakan meliputi variabel Particulate Matter. Particulate Matter (PM) adalah partikel udara. Variabel yang terdapat pada data yaitu PM2.5 dan PM10. Particulate Matter (PM2.5 dan PM10) adalah partikel udara yang berukuran lebih kecil dari atau sama dengan 2.5 dan 10 µm (mikrometer). Dari semua tindakan polusi udara, PM2.5 merupakan ancaman kesehatan terbesar. 1 Karena ukurannya yang kecil, PM2.5 dapat tetap melayang di udara untuk waktu yang lama dan dapat diserap jauh ke dalam aliran darah saat terhirup.</p>
                    <p>Beberapa sumber PM2.5 buatan manusia yang paling umum: </p>
                    <ul>
                    <li>Pembakaran motor</li>
                    <li>Pembakaran pembangkit listrik</li>
                    <li>Proses industri</li>
                    <li>Kompor, perapian, dan pembakaran kayu rumah</li>
                    <li>Asap dari kembang api</li>
                    <li>Merokok</li>
                    </ul>
                    <p>Sumber alami PM2.5 dapat meliputi: </p>
                    <ul>
                    <li>Debu</li>
                    <li>Jelaga</li>
                    <li>Kotoran</li>
                    <li>Garam tertiup angin</li>
                    <li>Spora tumbuhan</li>
                    <li>Serbuk sari</li>
                    <li>Asap dari kebakaran hutan</li>
                    </ul>
                    <p>Refrensi : <a href="https://www.iqair.com/id/newsroom/pm2-5">https://www.iqair.com/id/newsroom/pm2-5</a></p>
                    </div>
            """, unsafe_allow_html=True)
with tab3:
    # Informasi Tingkat PM2.5
    st.header('TABEL INFORMASI TINGKAT PM2.5')
    st.markdown("""Tabel rujukan nilai polusi PM2.5 adalah tabel yang memuat standar atau batasan yang ditetapkan oleh badan atau lembaga lingkungan untuk konsentrasi partikel PM2.5 dalam udara yang dianggap aman atau diterima untuk kesehatan manusia. 
             PM2.5 mengacu pada partikel halus berukuran 2,5 mikrometer atau lebih kecil yang terdapat di udara, dan dapat berasal dari berbagai sumber seperti polusi kendaraan, industri, pembakaran, atau debu. 
             Tabel rujukan nilai polusi PM2.5 ini biasanya ditetapkan oleh Organisasi Kesehatan Dunia (WHO), 
             atau badan lingkungan di negara tertentu. Nilai-nilai ini menunjukkan tingkat konsentrasi PM2.5 yang dianggap sebagai tingkat aman bagi kesehatan manusia.""")
    
    with st.expander("Lihat Penjelasan Selengkapnya"):
        
        image = Image.open('image/statistik.png')
        st.image(image)
    
        def read_markdown_file(markdown_file):
            return Path(markdown_file).read_text()
    
        intro_markdown = read_markdown_file("markdown/kesimpulan.md")
        st.markdown(intro_markdown, unsafe_allow_html=True)

    image = Image.open('image/pm25.jpeg')
    st.image(image) 