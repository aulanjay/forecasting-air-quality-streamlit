import streamlit as st
import pandas as pd
import pydeck as pdk
from geopy.geocoders import Nominatim

st.set_page_config(layout="wide")
st.title("ANALISIS KLUSTER LUASAN WILAYAH RTH DKI JAKARTA")

df_cluster = pd.read_csv("dataset/kluster.csv", index_col= 0)

st.bar_chart(df_cluster)
st.table(df_cluster)

# Load data
df_clustering = pd.read_csv("dataset/hasil_clustering_updated.csv")

# Peta hanya untuk DKI Jakarta
view = pdk.data_utils.compute_view(df_clustering[['longitude', 'latitude']])
view.pitch = 45

# Set warna berbeda untuk setiap cluster
color_scale = {
    0: [0, 255, 0],  # Hijau untuk Cluster 1
    1: [255, 0, 0],  # Merah untuk Cluster 2
    2: [0, 0, 255]   # Biru untuk Cluster 3
}

# Mendefinisikan fungsi untuk mendapatkan warna berdasarkan cluster
def get_color(cluster):
    return color_scale.get(cluster, [0, 0, 0])

# Menambahkan kolom warna pada DataFrame
df_clustering['color'] = df_clustering['cluster'].apply(get_color)

# Membuat layer peta
layer = pdk.Layer(
    "ScatterplotLayer",
    data=df_clustering,
    get_position=['longitude', 'latitude'],
    get_fill_color='color',
    get_radius=400,
    opacity=0.8,
    filled=True,
    pickable=True,  # Setel ke True
    radius_scale=5,
    radius_min_pixels=5,
    radius_max_pixels=30
)

# Menampilkan peta menggunakan Pydeck
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=view,
    layers=[layer]
))