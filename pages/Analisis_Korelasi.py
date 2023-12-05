import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.header("HUBUNGAN ANTARA RUANG TERBUKA HIJAU DENGAN PM2.5")

# Read dataset 
df_corr = pd.read_csv("dataset/hasil_korelasi.csv")
df_heatmap = pd.read_csv("dataset/hasil_korelasi_heatmap.csv")

# Ubah Tipe data dengan angka pecahan menjadi 2 angka desimal dibelakang koma
# df_corr = df_corr.applymap(lambda x: f'{x:.2f}' if pd.notna(x) and isinstance(x, (int, float)) else x)

# Menampilkan tabel yang berisi data dari dataset 
st.checkbox("Use container width", value=False, key="use_container_width")
st.dataframe(df_corr, use_container_width=st.session_state.use_container_width)

# Mengganti nama pada sumbu Y
yticklabels = df_heatmap.columns
yticklabels = ['Year', 'PM2.5', 'RTH']

# Menampilkan korelasi dengan menggunakan heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df_heatmap, annot=True, cmap="coolwarm", yticklabels=yticklabels)
plt.title("Heatmap Korelasi Antara Year vs PM 2.5 vs RTH")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()