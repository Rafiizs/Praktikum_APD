# Input nama, NIM, dan harga gula
nama = "Muhammad Rafii Zaidan Sakaria"
nim = "2409106095"
harga_gula = float(input("Masukkan harga gula: Rp "))

# Persentase diskon
diskon_gulaku = 7 / 100
diskon_manis_kita = 11 / 100
diskon_gunung_madu = 13 / 100

# Menghitung harga setelah diskon
harga_gulaku = harga_gula - (harga_gula * diskon_gulaku)
harga_manis_kita = harga_gula - (harga_gula * diskon_manis_kita)
harga_gunung_madu = harga_gula - (harga_gula * diskon_gunung_madu)

# Menampilkan hasil
print(f"Nama: {nama}")
print(f"NIM: {nim}")
print(f"Harga gula seharga gula: Rp {harga_gula}")
print(f"Jika membeli Gulaku, total yang harus dibayar setelah diskon 7%: Rp {harga_gulaku}")
print(f"Jika membeli Manis Kita, total yang harus dibayar setelah diskon 11%: Rp {harga_manis_kita}")
print(f"Jika membeli Gunung Madu, total yang harus dibayar setelah diskon 13%: Rp {harga_gunung_madu}")