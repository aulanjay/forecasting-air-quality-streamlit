# Panduan Penggunaan Streamlit 

## 1. Kebutuhan Software
* Unduh [Anaconda](https://www.anaconda.com/download)
* Unduh [Python 3.11.4](https://www.python.org/downloads/release/python-3114/)
* Unduh [Visual Studio Code](https://code.visualstudio.com/download)

## 2. Installasi Anaconda & Konfigurasi Path
* Lakukan instalasi anaconda seperti install software biasa, setelah selesai install jangan terlebih dahulu buka aplikasi Anaconda-nya.
* Pada search bar di windows cari "Anaconda Prompt" dan buka terminalnya.
* Ketik perintah `where conda` dan `where python` pada Anaconda Prompt lalu enter.
* Copy pada bagian Conda `C:\Users\Admin\anaconda3\Scripts\`, dan Copy juga pada bagian Python `C:\Users\Admin\anaconda3\`
* Buka search bar, ketik `Environment` buka "Buka edit system environment variables".
* Pilih tab Advance >> Environment Variabels >> Pada System Variables double klik bagian Path.
* Pilih New >> Paste path untuk Anaconda `C:\Users\Admin\anaconda3\Scripts\` >> Enter.
* Kemudian lakukan juga pada path Python Pilih New >> Paste path untuk Anaconda `C:\Users\Admin\anaconda3\` >> Enter. Kemudian OK.
* Untuk memastikan Python sudah terinstall di komputer, buka CMD >> ketik perintah berikut `python --version`.

## 3. Install Visual Studio Code
* Lakukan instalasi Visual Studio Code seperti biasa.
* Buka Visual Studio Code kemudian install ektensi untuk Python dan Jupyter Notebook.
* Setelah instalasi ekstensi selesai, buat file dengan format ipynb. Contoh : `example.ipynb`.
## 4. Konfigurasi Environment Streamlit
* pip freeze > requirements.txt
