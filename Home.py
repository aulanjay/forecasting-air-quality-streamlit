import streamlit as st
import pickle
import streamlit_authenticator as stauth
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
from pathlib import Path
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Beranda",
    page_icon="👋",
    layout="wide",
    )
# --- User login
names = ["Admin"]
usernames = ["admin"]

# --- load Hash password
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

# Mengatur Autentikasi dengan cookie
authenticator = stauth.Authenticate(
    names, usernames, hashed_passwords, "home", "1111", cookie_expiry_days=30
    ) # User dapat masuk ke halaman web dengan cookie dengan batas waktu 30 hari

name, authentication_status, username = authenticator.login("Login", "main")

# Kondisi saat User hendak login
if authentication_status == False:
    st.error("Username atau Password Salah")
    
if authentication_status == None:
    st.warning("Masukan Username dan Password Anda")
    
if authentication_status == True :
    st.sidebar.title(f"Selamat Datang {name}")
    authenticator.logout("Logout", "sidebar")
    
    # ---- Sidebar menu
    # with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "PM2.5 Introduction","Ruang Terbuka Hijau","Analisis Korelasi", "Analisis Kluster","Forcasting"],
        icons=["house-fill","cloud-fill","tree-fill","infinity","pie-chart-fill","bar-chart-line-fill"],
        menu_icon="cast",
        orientation="horizontal",
        default_index=0,
    )
        
    if selected == "Home":
        st.markdown("<h1 style='text-align: center;'>Aplikasi Prediksi Tingkat Polusi Udara DKI Jakarta</h1>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>Selayang Pandang Aplikasi</h2>", unsafe_allow_html=True)

        def read_markdown_file(markdown_file):
                return Path(markdown_file).read_text()
        intro_markdown = read_markdown_file("markdown/apk.md")
        st.markdown(intro_markdown, unsafe_allow_html=True)
        st.write("---")

        st.subheader("Pendahuluan :wave:")
                
        intro_markdown = read_markdown_file("markdown/pendahuluan.md")
        st.markdown(intro_markdown, unsafe_allow_html=True)
                
        st.write("---")
    if selected == "PM2.5 Introduction":
        tab1, tab2, tab3= st.tabs(["PM2.5 Emission In Jakarta", "Statistik Deskriptif", "Informasi Tingkat PM2.5"])

        # Tab 1
        with tab1:
            st.title("PM2.5 AIR POLUTION")

            st.header("PEMBAHASAN")
            st.markdown("Particulate Matter (PM2.5) adalah partikel udara yang berukuran lebih kecil dari atau sama dengan 2.5µm (mikrometer). Dari semua tindakan polusi udara, PM2.5 merupakan ancaman kesehatan terbesar. Karena ukurannya yang kecil, PM2.5 dapat tetap melayang di udara untuk waktu yang lama dan dapat diserap jauh ke dalam aliran darah saat terhirup.")

            st.header("PM2.5 EMISSION IN JAKARTA")

            # Membaca Dataset
            df = pd.read_csv('dataset/Mean_PM25 pertahun.csv')
            
            
            
            
            # ----------------- Path untuk file CSV & CRUD
            file_dir = r'd:\streamlit\login\dataset'
            file_name = 'Mean_PM25 pertahun.csv'
            file_path = f"{file_dir}/{file_name}"

            # Fungsi untuk membaca dan menulis data
            def read_data():
                return pd.read_csv(file_path)

            def write_data(df):
                df.to_csv(file_path, index=False)

            # Fungsi untuk menambahkan grafik line chart
            def line_chart(data, x_column, y_columns, title, xlabel, ylabel):
                plt.figure(figsize=(10, 6))
                for y_column in y_columns:
                    sns.lineplot(x=x_column, y=y_column, data=data, label=y_column, marker='o')

                plt.title(title)
                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
                plt.legend()
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.pyplot()

            # Fungsi untuk menambahkan data
            def add_data(df, new_year, new_pm25):
                new_data = {'year': new_year, 'pm25': new_pm25}
                df = df._append(new_data, ignore_index=True)
                write_data(df)
                st.success("Data berhasil ditambahkan!")
                return df

            # Fungsi untuk mengedit data
            def edit_data(df, selected_index, new_year, new_pm25):
                df.at[selected_index, 'year'] = int(new_year)
                df.at[selected_index, 'pm25'] = new_pm25
                write_data(df)
                st.success("Data berhasil diubah!")

            # Fungsi untuk menghapus data
            def delete_data(df, selected_index):
                df = df.drop(index=selected_index)
                write_data(df)
                st.success("Data berhasil dihapus!")
                return df
            
            # Halaman utama
            def main():
                df1 = read_data()

                # Pilihan aksi dalam selectbox
                action = st.sidebar.selectbox("Pilih Aksi", ["Tambah Data", "Edit Data", "Hapus Data"])

                # Tambah Data
                if action == "Tambah Data":
                    st.sidebar.header("Tambah Data Baru")
                    with st.sidebar.form(key='add_form'):
                        new_year = st.number_input('year', min_value=0.00)
                        new_pm25 = st.number_input('pm25', min_value=0.00)
                        submit_add = st.form_submit_button('Tambahkan Data')

                        if submit_add:
                            df1 = add_data(df1, new_year, new_pm25)

                # Edit Data
                elif action == "Edit Data":
                    st.sidebar.header("Edit Data")

                    selected_index_edit = st.sidebar.text_input("Nomor Baris yang Akan Diedit:")
                    selected_index_edit = int(selected_index_edit) if selected_index_edit.isdigit() else None

                    if selected_index_edit is not None and 0 <= selected_index_edit < len(df1):
                        selected_data_edit = df1.iloc[selected_index_edit]
                        
                        with st.sidebar.form(key='edit_form'):
                            new_year_edit = st.number_input('Masukan Tahun Baru:', value=selected_data_edit['year'])
                            new_pm25_edit = st.number_input('Masukan PM2.5 Baru:', value=selected_data_edit['pm25'])
                            submit_edit = st.form_submit_button('Edit Data')

                            if submit_edit:
                                edit_data(df1, selected_index_edit, new_year_edit, new_pm25_edit)
                    else:
                        st.warning("Nomor baris tidak valid. Harap masukkan nomor baris yang benar.")

                # Hapus Data
                elif action == "Hapus Data":
                    st.sidebar.header("Hapus Data")
                    with st.sidebar.form(key='delete_form'):
                        selected_index_delete = st.number_input('Pilih Nomor Baris Yang Akan Dihapus:', min_value=0, max_value=len(df1)-1, value=0)
                        # selected_data_delete = df1.iloc[selected_index_delete]
                        # st.write(f"Data Yang Dipilih: {selected_data_delete}")
                        submit_delete = st.form_submit_button('Hapus Data')

                        if submit_delete:
                            df1 = delete_data(df1, selected_index_delete)

                # Menampilkan grafik line chart
                st.write("### Dataset Polusi Udara DKI Jakarta")
                st.checkbox("Use container width", value=False, key="use_container_width")
                st.dataframe(df1, use_container_width=st.session_state.use_container_width)
                line_chart(df1, 'year', ['pm25'], 'Line Chart', 'Year', 'PM2.5')

            # Menjalankan aplikasi
            if __name__ == '__main__':
                main()
                
                
                
                
            # # Tambahkan checkbox untuk setiap tahun
            # selected_years = st.multiselect('Pilih Tahun', df['year'].unique())

            # # Filter dataset berdasarkan tahun yang dipilih
            # filtered_data = df[df['year'].isin(selected_years)]

            # # Tampilkan grafik PM2.5 per tahun berdasarkan checkbox
            # if not filtered_data.empty:
            #     st.write('### Grafik PM2.5 per Tahun')
            #     plt.figure(figsize=(10, 6))
            #     sns.lineplot(x='year', y='pm25', data=filtered_data, marker='o')
            #     plt.xlabel('Tahun')
            #     plt.ylabel('PM2.5')
            #     plt.title('Grafik PM2.5 per Tahun')
            #     st.pyplot()
            # else:
            #     st.warning('Data untuk tahun yang dipilih tidak tersedia.')
            #     st.set_option('deprecation.showPyplotGlobalUse', False)

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
                            <p style="text-align:justify;">Statisika Deskriptif meliputi nilai rata-rata (mean), median, modus, deviasi standar, kuartil, rentang, dan sebagainya. Statistik ini membantu memberikan gambaran umum tentang distribusi data. Kali ini akan dianalisis mengenai variabel pm2.5 dan pm10 yang digunakan.</p>
                            <p style="text-align:justify;">Exploratory Data Analysis. Ini adalah proses dalam analisis data yang bertujuan untuk menjelajahi dan memahami struktur, pola, serta karakteristik dari data yang tersedia. Data yang digunakan meliputi variabel Particulate Matter. Particulate Matter (PM) adalah partikel udara. Variabel yang terdapat pada data yaitu PM2.5 dan PM10. Particulate Matter (PM2.5 dan PM10) adalah partikel udara yang berukuran lebih kecil dari atau sama dengan 2.5 dan 10 µm (mikrometer). Dari semua tindakan polusi udara, PM2.5 merupakan ancaman kesehatan terbesar. 1 Karena ukurannya yang kecil, PM2.5 dapat tetap melayang di udara untuk waktu yang lama dan dapat diserap jauh ke dalam aliran darah saat terhirup.</p>
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
    if selected == "Ruang Terbuka Hijau":
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

        # Menampilkan tabel Statistik 
        st.write("### STATISTIKA DESKRIPTIF")
        st.table({
            'Informasi' : ['Standar Deviasi', 'Rata-Rata Luas RTH', 'Nilai Minimum', 'Nilai Maximum'],
            'Luas RTH' : [std_deviasi, avg_luas_rth, min_luas_rth, max_luas_rth],
        })
    if selected == "Analisis Korelasi":
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
    if selected == "Analisis Kluster":
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

    if selected == "Forcasting":
        st.markdown("<h1 style='text-align: center;'>FORECASTING PM 2.5</h1>", unsafe_allow_html=True)
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

        with st.expander("Lihat Penjelasan Selengkapnya"):
            def read_markdown_file(markdown_forecast):
                return Path(markdown_forecast).read_text()
            forecast = read_markdown_file("markdown/forecast.md")
            st.markdown(forecast, unsafe_allow_html=True)

    
    
    
    
    
    
    
