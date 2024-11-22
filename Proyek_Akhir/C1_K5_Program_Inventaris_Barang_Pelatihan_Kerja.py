import os
os.system('color')
from termcolor import colored
from prettytable import PrettyTable

# Fungsi untuk membersihkan layar
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# Database sederhana untuk akun dan inventaris barang
Akun = {}
inventaris = {
    "mixer": {"harga": 157000, "jumlah": 1, "kondisi": "layak"},
    "pengaduk manual": {"harga": 12000, "jumlah": 1, "kondisi": "layak"},
    "oven": {"harga": 550000, "jumlah": 1, "kondisi": "layak"},
    "loyang": {"harga": 25000, "jumlah": 1, "kondisi": "layak"},
    "cetakan kue": {"harga": 160000, "jumlah": 1, "kondisi": "layak"},
    "saringan": {"harga": 16000, "jumlah": 1, "kondisi": "layak"},
}

# Fungsi Untuk Membuat Table Inventaris
def tabel_inventaris():
    table = PrettyTable()
    table.field_names = ["Barang", "Harga", "Jumlah", "Kondisi"]
    for barang, detail in inventaris.items():
        table.add_row([barang, detail["harga"], detail["jumlah"], detail["kondisi"]])
    return table


# Fungsi Untuk Membuat Akun Baru
def Buat_Akun():
    cls()
    print("=== Buat Akun ===")
    while True:
        username = input("Masukkan username (Maksimal 5 karakter): ")
        if len(username) > 5:
            print(colored("Username tidak boleh lebih 5 karakter!\n", "red"))
            continue
        
        if username in Akun:
            print(colored("Username sudah terdaftar!.\n", "red"))
            continue

        break

    while True:
        password = input("Masukkan password (Maksimal 5 karakter): ")
        if len(password) > 5:
            print(colored("Password tidak boleh lebih 5 karakter!\n", "red"))
            continue

        break
    
    Akun[username] = password
    print(colored("Akun berhasil dibuat!\n", "green"))
    input("Tekan Enter untuk kembali")


# Fungsi Untuk Login 
def login():
    cls()
    print("=== Login ===")
    username = input("Masukkan username (Maksimal 5 karakter): ")
    if len(username) > 5:
        print(colored("Username tidak boleh lebih 5 karakter!\n", "red"))
        input("Tekan Enter untuk kembali.")
        login()
        return False
    
    password = input("Masukkan password Maksimal 5 karakter): ")
    if len(password) > 5:
        print(colored("Password tidak boleh lebih 5 karakter!\n", "red"))
        input("Tekan Enter untuk kembali.")
        login()
        return False
    
    if Akun.get(username) == password:
        print(colored("Login berhasil!\n", "green"))
        input("Tekan Enter untuk melanjutkan.")
        return True
    else:
        print("Username atau password salah!\n")
        input("Tekan Enter untuk kembali.")
        return False


# Fungsi Untuk Menampilkan Inventaris
def Tampilkan_Barang():
    print("=== Daftar Barang ===")
    if not inventaris:
        print("Inventaris kosong.\n")
    else:
        print(tabel_inventaris())
    print()


# Fungsi Untuk Menambahkan Barang
def Tambah_Barang():
    cls()
    Tampilkan_Barang()
    print("=== Tambah Barang ===")
    nama = input("Nama barang: ").lower()
    while True:
        try:
            jumlah = int(input("Jumlah barang (Maksimal 100): "))
            if jumlah > 100:
                print(colored("Jumlah barang tidak boleh melebihi 100", "red"))
                continue
            harga = int(input("Harga barang: Rp"))
            kondisi = input("Kondisi barang (layak/tidak layak): ").lower()
            if kondisi not in ["layak", "tidak layak"]:
                print(colored("Masukkan 'layak' atau 'tidak layak' untuk kondisi barang", "red"))
                continue
            break
        except ValueError:
            print(colored("Masukkan angka untuk jumlah dan harga!", "red"))
    
    inventaris[nama] = {
        "harga": harga,
        "jumlah": jumlah,
        "kondisi": kondisi
    }
    print(f"{jumlah} {nama} berhasil ditambahkan dengan kondisi '{kondisi}'!\n")


# Fungsi Untuk Menampilkan Barang
def show_inventaris():
    cls()
    Tampilkan_Barang()
    input("Tekan Enter untuk kembali.")


# Fungsi Untuk Update Barang
def Update_Barang():
    cls()
    Tampilkan_Barang()
    print("=== Update Barang ===")
    barang = input("Masukkan nama barang yang ingin diupdate: ").lower()
    if barang in inventaris:
        while True:
            try:
                jumlah = int(input("Masukkan jumlah barang baru (Maksimal 100): "))
                if jumlah > 100:
                    print("Jumlah barang tidak boleh melebihi 100.")
                    continue
                harga_baru = int(input(f"Masukkan harga baru untuk {barang}: Rp"))
                kondisi_baru = input("Masukkan kondisi baru (layak/tidak layak): ").lower()
                if kondisi_baru not in ["layak", "tidak layak"]:
                    print("Masukkan 'layak' atau 'tidak layak' untuk kondisi barang.")
                    continue
                inventaris[barang] = {"harga": harga_baru, "jumlah": jumlah, "kondisi": kondisi_baru}
                print(colored(f"{barang} berhasil diupdate.\n", "green"))
                break
            except ValueError:
                print("Masukkan angka yang benar.")
                Update_Barang()
    else:
        print(colored("Barang tidak ditemukan.\n", "red"))
    input("Tekan Enter untuk kembali.")
    menu_inventaris()


# Fungsi Untuk Menghapus Barang
def Hapus_Barang():
    cls()
    Tampilkan_Barang()
    print("=== Hapus Barang ===")
    barang = input("Masukkan nama barang yang ingin dihapus: ").lower()
    if barang in inventaris:
        del inventaris[barang]
        print(colored(f"{barang} berhasil dihapus dari inventaris.\n", "green"))
    else:
        print(colored("Barang tidak ditemukan dalam inventaris.\n", "red"))
    input("Tekan Enter untuk kembali.")
    menu_inventaris()


# Fungsi ini Menu Utama Pengguna dapat memilih opsi
def main():
    while True:
        cls()
        print("=== Menu Utama ===")
        print("1. Buat Akun")
        print("2. Login")
        print("3. Keluar")
        
        pilihan = input("Pilih opsi (1-3): ")
        
        if pilihan == '1':
            Buat_Akun()
        elif pilihan == '2':
            if login():
                menu_inventaris()
        elif pilihan == '3':
            print(colored("Terima kasih! Program selesai.", "yellow"))
            break
        else:
            print(colored("Opsi tidak valid.", "red"))
            input("Tekan Enter untuk kembali.")


# Fungsi Menu Inventaris di mana pengguna yg sudah login dapat memilih opsi dari inventaris
def menu_inventaris():
    while True:
        cls()
        print("=== Menu Inventaris ===")
        print("1. Tambah Barang")
        print("2. Lihat Inventaris")
        print("3. Update Barang")
        print("4. Hapus Barang")
        print("5. Logout")
        
        pilihan = input("Pilih opsi (1-5): ")
        
        if pilihan == '1':
            Tambah_Barang()
        elif pilihan == '2':
            show_inventaris()
        elif pilihan == '3':
            Update_Barang()
        elif pilihan == '4':
            Hapus_Barang()
        elif pilihan == '5':
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali.")


main()