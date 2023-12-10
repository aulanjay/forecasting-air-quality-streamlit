import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import streamlit as st

st.set_page_config(
    layout="wide",
    page_icon=":deciduous_tree:",
    page_title="Ruang Terbuka Hijau")
st.markdown("<h1 style='text-align: center; color: green;'>RUANG TERBUKA HIJAU</h1>", unsafe_allow_html=True)
st.write("#### Menurut Undang-Undang No. 26 tahun 2007 tentang Penataan Ruang, pengertian ruang terbuka hijau (RTH) adalah area memanjang / jalur dan / atau mengelompok, yang penggunaannya lebih bersifat terbuka, tempat tumbuh tanaman, baik yang tumbuh alamiah maupun sengaja ditanam.")

st.header("Rata-Rata Ruang Terbuka Hijau (RTH) di Jakarta")
col1, col2 = st.columns(2)

df = pd.read_csv("dataset/rthbaru.csv")

with col2:
    # Cek dan hapus koma pada kolom 'tahun' jika ada
    df['tahun'] = df['tahun'].replace(',', '', regex=True)

    # Konversi kolom 'tahun' ke tipe data numerik
    df['tahun'] = pd.to_numeric(df['tahun'], errors='coerce').astype(int)

    # Ganti format tahun menjadi 4 digit
    df['tahun'] = df['tahun'].apply(lambda x: f'{x:04d}')

    # Hitung rata-rata RTH per tahun
    avg_rth_per_year = df.groupby('tahun')['luas wilayah rth (km2)'].mean().reset_index()

   # Tampilkan hasil
    st.table(avg_rth_per_year)

with col1:
    # Tampilkan rata-rata RTH dalam grafik dengan altair
    chart = alt.Chart(avg_rth_per_year).mark_line(point=True).encode(
        x='tahun:N',
        y = alt.Y('luas wilayah rth (km2):Q', scale=alt.Scale(domain=[100, 120]), title='Rata-rata Luas Wilayah RTH (km2)'),
        tooltip=['tahun:N', 'luas wilayah rth (km2):Q']
    ).properties(
        width=600,
        height=400,
        title='Grafik Rata-rata Luas Wilayah RTH per tahun di Jakarta'
    )

    # Tampilkan grafik altair
    st.altair_chart(chart, use_container_width=True)

# Menghitung nilai luas RTH
sum_rth = df['luas wilayah rth (km2)'].sum()
std_deviasi = 145.553
avg_luas_rth = df['luas wilayah rth (km2)'].mean()
min_luas_rth = df['luas wilayah rth (km2)'].min()
max_luas_rth = df['luas wilayah rth (km2)'].max()
# st.table([sum_rth])

# # Filter baris dengan luas wilayah RTH yang bukan 0
# df_filtered = df[df['luas wilayah rth (km2)'] != 0]

# # Tampilkan hasil dalam bentuk tabel
# st.dataframe(df_filtered)

# # Tampilkan diagram lingkaran (pie chart) menggunakan matplotlib
# plt.figure(figsize=(10, 8))
# plt.pie(df_filtered['luas wilayah rth (km2)'], labels=df_filtered['kota/kabupaten'], autopct='%1.1f%%', startangle=140)
# plt.axis('equal')  # Memastikan diagram lingkaran tampak lingkaran sempurna
# plt.title(f'Diagram Lingkaran Luas Wilayah RTH di Jakarta ({sum_rth:.2f} km2)')
# st.pyplot()


# Menampilkan tabel Statistik 
st.write("### STATISTIKA DESKRIPTIF")
st.table({
    'Informasi' : ['Standar Deviasi', 'Rata-Rata Luas RTH', 'Nilai Minimum', 'Nilai Maximum'],
    'Luas RTH' : [std_deviasi, avg_luas_rth, min_luas_rth, max_luas_rth],
})




# # Tampilkan rata-rata RTH dalam grafik
# plt.figure(figsize=(10, 6))
# sns.lineplot(x='tahun', y='luas wilayah rth (km2)', data = avg_rth_per_year, marker= 'o')
# plt.xlabel('Tahun')
# plt.ylabel('Rata-rata % RTH (b/a)')
# plt.title('Grafik Rata-rata RTH per tahun di Jakarta')
