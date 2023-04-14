import streamlit as st
from streamlit_option_menu import option_menu

st.write("""
#Aplikasi Menghitung Luas Bangun
ini adalah aplikasi menghitung luas Bangun sederhana menggunakan streamlit
""")

#Navigas sidebar
with st.sidebar :
  selected = option_menu ('Hitung Luas Bangunan', ['Hitung Luas Persegi Panjang', 'Hitung Luas Segitiga'],
  default_index=0)

#Halaman Hitung Luas Persegi Panjang
if (selected =='Hitung Luas Persegi Panjang'):
  st.title('Hitung Luas Persegi Panjang')
  
  alas = st.number_input("Masukan Alas", 0)
  tinggi = st.number_input("Masukan Tinggi", 0)
  hitung = st.button("Hitung Luas")

  if hitung:
    luas = alas * tinggi
    st.success(f"Luas persegi panjangnya adalah {luas}")
# Halaman Hitung Luas Segitiga    
if (selected =='Hitung Luas Segitiga'):
  st.title('Hitung Luas Segitiga')

  alas = st.number_input("Masukan Nilai Alas")
  tinggi = st.number_input("Masukan Nilai Tinggi")
  hitung = st.button("Hitung Luas")

  if hitung:
    luas = 0.5 * alas * tinggi
    st.success(f" Luas segitiganya adalah {luas}")