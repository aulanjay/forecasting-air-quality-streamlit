import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.title("PM2.5 AIR POLUTION")

st.header("SOURCE")
st.caption("Particulate Matter (PM2.5) adalah partikel udara yang berukuran lebih kecil dari atau sama dengan 2.5µm (mikrometer).")
st.caption("Dari semua tindakan polusi udara, PM2.5 merupakan ancaman kesehatan terbesar. Karena ukurannya yang kecil, PM2.5 dapat tetap melayang di udara untuk waktu yang lama dan dapat diserap jauh ke dalam aliran darah saat terhirup.")

st.header("PM2.5 EMISSION IN JAKARTA")

# Membaca Dataset
df = pd.read_csv('dataset/Mean_PM25 pertahun.csv')


# Tambahkan checkbox untuk setiap tahun
selected_years = st.multiselect('Pilih Tahun', df['year'].unique())

# Filter dataset berdasarkan tahun yang dipilih
filtered_data = df[df['year'].isin(selected_years)]

# Tampilkan grafik PM2.5 per tahun berdasarkan checkbox
if not filtered_data.empty:
    st.write('### Grafik PM2.5 per Tahundddd')
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='year', y='pm25', data=filtered_data, marker='o')
    plt.xlabel('Tahun')
    plt.ylabel('PM2.5')
    plt.title('Grafik PM2.5 per Tahun')
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)
else:
    st.warning('Data untuk tahun yang dipilih tidak tersedia.')

# # Menampilkan Grafik PM25 Pertahun
# st.write('### Grafik PM2.5 per Tahun')
# plt.figure(figsize=(10, 6))
# sns.lineplot(x='year', y='pm25', data=df, marker='o')
# plt.xlabel('Tahun')
# plt.ylabel('PM2.5')
# plt.title('Grafik PM2.5 per Tahun')
# st.pyplot()
# st.set_option('deprecation.showPyplotGlobalUse', False)

# Menghitung Nilai PM2.5
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

# Informasi Tingkat PM2.5
st.write('### TABEL INFORMASI TINGKAT PM2.5')
image = Image.open('image/20230122_190802.jpg')
st.image(image) 