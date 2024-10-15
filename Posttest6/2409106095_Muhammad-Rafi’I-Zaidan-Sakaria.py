Manga_List = {
    1: {"judul": "One Piece", "harga": 50000, "Genre": ["Adventure", "Action"]},
    2: {"judul": "Naruto", "harga": 45000, "Genre": ["Adventure", "Action"]},
    3: {"judul": "Attack on Titan", "harga": 60000, "Genre": ["Adventure", "Fantasy", "Martial Arts"]},
    4: {"judul": "My Hero Academia", "harga": 55000, "Genre": ["Action", "Drama", "Fantasy"]},
    5: {"judul": "Demon Slayer", "harga": 65000, "Genre": ["Action", "Superhero", "School"]},
    6: {"judul": "Jujutsu Kaisen", "harga": 60000, "Genre": ["Action", "Supernatural", "School"]},
    7: {"judul": "Spy x Family", "harga": 40000, "Genre": ["Comedy", "Action", "Slice of Life"]},
    8: {"judul": "Tokyo Revengers", "harga": 55000, "Genre": ["Action", "Drama", "Supernatural"]},
    9: {"judul": "Hunter x Hunter", "harga": 50000, "Genre": ["Adventure", "Fantasy", "Shounen"]},
    10: {"judul": "Fullmetal Alchemist", "harga": 55000, "Genre": ["Adventure", "Action", "Fantasy"]}
}

akuns = {}

while True:
    print("Selamat Datang di Pembelian! Mau beli apa?")
    print("Silakan pilih 'Sign Up' jika belum buat akun, dan jika sudah memiliki akun silahkan 'Login'")
    print("1. Sign Up")
    print("2. Login")
    print("3. Exit")
    print("――――――――――――――――――――――――")
    opsi = input("Pilih opsi: ")
    print(" ")

    if opsi == "1":
        print("Halo! Silahkan Registrasi dulu")
        Username = input("Username: ")

        if Username in akuns:
            print("Nama Sudah Terpakai. Silahkan Coba Lagi")
        else:
            Password = input("Password: ")
            akuns[Username] = {"Password": Password, "Keranjang": []}
            print(f"Akun Anda berhasil terdaftar dengan ID: {Username}")

    elif opsi == "2":
        print("Hallo, silahkan masukkan akun anda!")
        Username = input("Username: ")
        Password = input("Password: ")

        if Username == "Admin" and Password == "Admin123":
            while True:  # sesi admin
                print("="*20)
                print("Selamat datang di sesi admin :)")
                print("===== Silahkan pilih Opsi =====")
                print("1. Melihat list akun dan daftar Keranjang")
                print("2. Hapus akun")
                print("3. Log out")

                adminOpsi = input("Pilih opsi: ")
                print(" ")

                if adminOpsi == "1":
                    print("Daftar Akun:")
                    for user in akuns:
                        print(user)
                elif adminOpsi == "2":
                    username_hapus = input("Masukkan username yang ingin dihapus: ")
                    if username_hapus in akuns:
                        del akuns[username_hapus]
                        print(f"Akun '{username_hapus}' telah dihapus.")
                    else:
                        print("Akun tidak ditemukan.")
                elif adminOpsi == "3":
                    print("Logout berhasil. Terima kasih!")
                    break
                else:
                    print("Opsi tidak valid. Silahkan coba lagi.")

        elif Username in akuns and akuns[Username]["Password"] == Password:
            while True:
                print("="*20)
                print(f"Selamat Datang {Username}")
                print("===== Silahkan Pilih Opsi =====")
                print("1. Lihat Daftar Manga")
                print("2. Tambah Ke Keranjang")
                print("3. Lihat Keranjang")
                print("4. Hapus Dari Keranjang")
                print("5. Selesaikan Pembelian")
                print("6. Logout")
                print("="*20)

                status = input("Pilih Opsi: ")
                print(" ")

                if status == "1":
                    print("Daftar Manga yang Tersedia:")
                    for key, manga in Manga_List.items():
                        print(f"{key}. {manga['judul']} - Rp{manga['harga']} - Genre: {', '.join(manga['Genre'])}")

                elif status == "2":
                    print("Daftar Manga yang Tersedia:")
                    for key, manga in Manga_List.items():
                        print(f"{key}. {manga['judul']} - Rp{manga['harga']} - Genre: {', '.join(manga['Genre'])}")
                    try:
                        pilihan_manga = int(input("Masukkan nomor manga yang ingin dibeli ke keranjang: "))
                        if pilihan_manga in Manga_List:
                            akuns[Username]["Keranjang"].append(Manga_List[pilihan_manga])
                            print(f" '{Manga_List[pilihan_manga]['judul']}' sudah masuk di keranjang")
                        else:
                            print("Nomor tidak valid.")
                    except ValueError:
                        print("Input tidak valid. Harap masukkan nomor yang benar.")

                elif status == "3":
                    if not akuns[Username]["Keranjang"]:
                        print("Anda belum membeli apa-apa.")
                    else:
                        print("Daftar di Keranjang:")
                        total_harga = 0
                        for indeks, manga in enumerate(akuns[Username]["Keranjang"], start=1):
                            print(f"{indeks}. {manga['judul']} - Rp{manga['harga']}")
                            total_harga += manga['harga']
                        print(f"Total harga: Rp{total_harga}")

                elif status == "4":
                    if not akuns[Username]["Keranjang"]:
                        print("Keranjang Anda kosong.")
                    else:
                        print("Daftar di Keranjang:")
                        for indeks, manga in enumerate(akuns[Username]["Keranjang"], start=1):
                            print(f"{indeks}. {manga['judul']} - Rp{manga['harga']}")
                        try:
                            manga_hapus = int(input("Masukkan nomor manga yang ingin dihapus: ")) - 1
                            if 0 <= manga_hapus < len(akuns[Username]["Keranjang"]):
                                removed_manga = akuns[Username]["Keranjang"].pop(manga_hapus)
                                print(f" '{removed_manga['judul']}' telah dihapus dari keranjang")
                            else:
                                print("Nomor tidak valid.")
                        except ValueError:
                            print("Input tidak valid. Harap masukkan nomor yang benar.")

                elif status == "5":
                    if not akuns[Username]["Keranjang"]:
                        print("Keranjang Anda kosong. Tidak ada yang bisa dibayar.")
                    else:
                        print("Daftar di Keranjang:")
                        total_harga = 0
                        for indeks, manga in enumerate(akuns[Username]["Keranjang"], start=1):
                            print(f"{indeks}. {manga['judul']} - Rp{manga['harga']}")
                            total_harga += manga['harga']
                        print(f"Total harga: Rp{total_harga}")
                        konfirmasi = input("Apakah Anda ingin menyelesaikan pembelian? (ya/tidak): ").lower()
                        if konfirmasi == "ya":
                            print("Pembelian Anda telah berhasil. Terima kasih sudah berbelanja!")
                            akuns[Username]["Keranjang"].clear()  # Mengosongkan keranjang setelah pembelian
                        else:
                            print("Pembelian dibatalkan.")

                elif status == "6":
                    print("Logout berhasil. Terima kasih!")
                    break

                else:
                    print("Opsi tidak valid. Silahkan coba lagi.")
        else:
            print("Username atau Password salah. Silahkan coba lagi.")

    elif opsi == "3":
        print("Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
        break

    else:
        print("Opsi tidak valid. Silahkan coba lagi.")