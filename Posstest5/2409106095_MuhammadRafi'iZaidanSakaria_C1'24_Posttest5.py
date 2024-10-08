anime_list = [
    {"judul": "One Piece", "harga": 50000},
    {"judul": "Naruto", "harga": 45000},
    {"judul": "Attack on Titan", "harga": 60000},
    {"judul": "My Hero Academia", "harga": 55000},
    {"judul": "Demon Slayer", "harga": 65000},
    {"judul": "Jujutsu Kaisen", "harga": 60000},
    {"judul": "Spy x Family", "harga": 40000},
    {"judul": "Tokyo Revengers", "harga": 55000},
    {"judul": "Hunter x Hunter", "harga": 50000},
    {"judul": "Fullmetal Alchemist", "harga": 55000}
]

accounts = []

while True:
    print("Selamat Datang di Pembelian Anime! Mau beli apa?")
    print("Silakan pilih 'Sign Up' jika belum buat akun, dan jika sudah memiliki akun silahkan 'Login'")
    print("1. Sign Up")
    print("2. Login")
    print("3. Exit")
    print("――――――――――――――――――――――――")
    opsi = input("Pilih opsi: ")
    print(" ")

    if opsi == "1":
        print("Selamat Datang! Sign Up dulu yah")
        Username = input("Masukkan Username: ")
        account_exists = False
        for account in accounts:
            if account[0] == Username:
                account_exists = True
                break
        if account_exists:
            print("Username telah terpakai, silahkan coba lagi.")
        else:
            Password = input("Masukkan Password: ")
            accounts.append([Username, Password, []])
            print(f"Account Anda telah terdaftar dengan nama {Username}")

    elif opsi == "2":
        print("Silahkan Login")
        Username = input("Masukkan Username: ")
        Password = input("Masukkan Password: ")
        user_found = False
        for account in accounts:
            if account[0] == Username and account[1] == Password:
                user_found = True
                while True:
                    print(f"Selamat Datang {Username}")
                    print("***** Silahkan Pilih Opsi *****")
                    print("1. Lihat Daftar Anime")
                    print("2. Tambah Anime Ke Keranjang")
                    print("3. Lihat Keranjang")
                    print("4. Hapus Anime Dari Keranjang")
                    print("5. Selesaikan Pembelian")
                    print("6. Logout")
                    print("*******************************")

                    status = input("Pilih Opsi: ")
                    print(" ")

                    if status == "1":
                        print("Daftar Anime yang Tersedia:")
                        for indeks, anime in enumerate(anime_list, start=1):
                            print(f"{indeks}. {anime['judul']} - Rp{anime['harga']}")

                    elif status == "2":
                        print("Daftar Anime yang Tersedia:")
                        for indeks, anime in enumerate(anime_list, start=1):
                            print(f"{indeks}. {anime['judul']} - Rp{anime['harga']}")
                        try:
                            pilihan_anime = int(input("Masukkan nomor anime yang ingin di beli ke keranjang: ")) - 1
                            if 0 <= pilihan_anime < len(anime_list):
                                account[2].append(anime_list[pilihan_anime])
                                print(f"Anime '{anime_list[pilihan_anime]['judul']}' sudah masuk di keranjang")
                            else:
                                print("Nomor tidak valid.")
                        except ValueError:
                            print("Input tidak valid. Harap masukkan nomor yang benar.")

                    elif status == "3":
                        if not account[2]:
                            print("Anda belum membeli apa-apa.")
                        else:
                            print("Daftar Anime di Keranjang:")
                            total_harga = 0
                            for indeks, anime in enumerate(account[2], start=1):
                                print(f"{indeks}. {anime['judul']} - Rp{anime['harga']}")
                                total_harga += anime['harga']
                            print(f"Total harga: Rp{total_harga}")

                    elif status == "4":
                        if not account[2]:
                            print("Keranjang Anda kosong.")
                        else:
                            print("Daftar Anime di Keranjang:")
                            for indeks, anime in enumerate(account[2], start=1):
                                print(f"{indeks}. {anime['judul']} - Rp{anime['harga']}")
                            try:
                                anime_hapus = int(input("Masukkan nomor anime yang ingin dihapus: ")) - 1
                                if 0 <= anime_hapus < len(account[2]):
                                    removed_anime = account[2].pop(anime_hapus)
                                    print(f"Anime '{removed_anime['judul']}' telah dihapus dari keranjang")
                                else:
                                    print("Nomor tidak valid.")
                            except ValueError:
                                print("Input tidak valid. Harap masukkan nomor yang benar.")

                    elif status == "5":
                        if not account[2]:
                            print("Keranjang Anda kosong. Tidak ada yang bisa dibayar.")
                        else:
                            print("Daftar Anime di Keranjang:")
                            total_harga = 0
                            for indeks, anime in enumerate(account[2], start=1):
                                print(f"{indeks}. {anime['judul']} - Rp{anime['harga']}")
                                total_harga += anime['harga']
                            print(f"Total harga: Rp{total_harga}")
                            konfirmasi = input("Apakah Anda ingin menyelesaikan pembelian? (ya/tidak): ").lower()
                            if konfirmasi == "ya":
                                print("Pembelian Anda telah berhasil. Terima kasih sudah berbelanja!")
                                account[2].clear()  # Mengosongkan keranjang setelah pembelian
                            else:
                                print("Pembelian dibatalkan.")

                    elif status == "6":
                        print("Logout berhasil. Terima kasih!")
                        break

                    else:
                        print("Opsi tidak valid. Silahkan coba lagi.")
                break
        if not user_found:
            print("Username atau Password salah. Silahkan coba lagi.")

    elif opsi == "3":
        print("Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
        break

    else:
        print("Opsi tidak valid. Silahkan coba lagi.")
