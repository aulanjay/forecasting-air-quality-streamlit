import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide",
                   page_icon=":chart_with_upwards_trend:")
st.title("FORECASTING PM 2.5")
st.header("Prediksi PM 2.5 Pertahun")

# Membaca dataset
df_forecast = pd.read_csv("dataset/forecast.csv")

# Mengubah kolom 'year' menjadi indeks
df_forecast.set_index("year", inplace=True)

# Membuat plot garis untuk actual, forecasting, min, dan max
st.write("Visualisasi Grafik Garis:")
fig, ax = plt.subplots(figsize=(15, 6))
df_forecast[["actual", "forecasting"]].plot(kind="line", ax=ax, label=["Actual", "Forecasting"])
plt.plot(df_forecast.index, df_forecast["Min"], label="Min", linestyle="--", color="red")
plt.plot(df_forecast.index, df_forecast["Max"], label="Max", linestyle="--", color="green")
plt.xticks(df_forecast.index.astype(int))  # Mengatur tahun pada sumbu x tanpa desimal
plt.xlabel("Year")
plt.ylabel("Value")
plt.title("Actual, Forecasting, Min, and Max Over Years")
plt.legend()
st.pyplot(fig)
























# df_forecasting = pd.read_csv("predicted_vs_actual.csv")

# # Set index ke kolom "Year"
# df_forecasting.set_index("Year", inplace=True)

# # Buat plot dengan Matplotlib
# fig, ax = plt.subplots()
# ax.plot(df_forecasting.index, df_forecasting["Actual_PM25"], label="Actual PM2.5", marker='o')
# ax.plot(df_forecasting.index, df_forecasting["Predicted_PM25"], label="Predicted PM2.5", marker='o')

# # Atur label dan judul
# ax.set_xlabel("Year")
# ax.set_ylabel("PM2.5")
# ax.set_title("Actual vs Predicted PM2.5")

# # Tampilkan legenda
# ax.legend()

# # Tampilkan plot di Streamlit
# st.pyplot(fig)

# # Tampilkan tabel
# st.subheader("Data PM2.5")
# st.table(df_forecasting)