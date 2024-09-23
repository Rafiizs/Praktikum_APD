Nama = input("Nama Pembeli : ")
Hari = input("senin,selas, rabu, kamis, jumat, sabtu, minggu : Hari ")
uang = float (input("Masukkan Harga Uang : Rp "))

if Hari == "senin" or "selasa" or "rabu" or "kamis" :
    Harga_Tiket = 40000 
    if uang >= Harga_Tiket :
        print(f"selamat {Nama} anda membeli tiket pada hari {Hari}")
    else : 
        print("uang anda tidak cukup")
elif Hari == "jumat" :
    Harga_Tiket = 45000
    if uang >= Harga_Tiket :
        print(f"selamat {Nama} anda membeli tiket pada hari {Hari}")
    else :
        print("uang anda tidak cukup")
elif Hari == "sabtu" :
    Harga_Tiket : 55000
    if uang >= Harga_Tiket :
        print(f"selamat {Nama} anda membeli tiket pada hari {Hari}")
    else :
        print("uang anda tidak cukup")
elif Hari == "minggu" :
    Harga_Tiket = 60000
    if uang >= Harga_Tiket :
        print(f"selamat {Nama} anda membeli tiket pada hari {Hari}")
    else :
        print("uang anda tidak cukup")
else :
    print(f"tidak valid")