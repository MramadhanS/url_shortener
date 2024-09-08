# Import library yang diperlukan
import streamlit as st
import pyshorteners

# Judul aplikasi
st.title("URL Shortener")

# Input URL dari pengguna
url = st.text_input("Masukkan URL yang ingin dipendekkan:")

# Buat objek pyshorteners
s = pyshorteners.Shortener()

# Fungsi untuk memendekkan URL
if st.button("Pendekkan URL"):
    if url:
        short_url = s.tinyurl.short(url)
        st.success(f"URL yang dipendekkan: {short_url}")
    else:
        st.error("Masukkan URL yang valid!")
