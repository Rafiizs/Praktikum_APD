loop = 0
while loop < 3:
    username = input("Masukan Username Anda : ")
    password = int(input("Masukan Password Anda : "))
    if username == "Rafii" and password == 95:
        lanjut = input("Apakah Anda Ingin Melanjutlan? (iya/tidak) : ")
        if lanjut == "iya" or lanjut == "tidak":
            hari = input("masukan hari : ")
            if hari == "senin" or hari == "selasa" or hari == "rabu" or hari == "kamis":
                uang = int(input("masukan harga uang : Rp "))
                hargatiket = 40000
                if uang >= hargatiket:
                    print(f"selamat {username} anda membeli tiket pada hari {hari}")
                    break
                else:
                    print("uang anda tidak cukup")
                    break
            else:
                if hari == "jumat":
                    uang = int(input())
                    hargatiket = 45000
                    if uang >= hargatiket:
                        print(f"selamat {username} anda membeli tiket pada hari {hari}")
                        break
                    else:
                        print("uang anda tidak cukup")
                        break
                else:
                    if hari == "sabtu":
                        uang = int(input())
                        hargatiket = 55000
                        if uang >= hargatiket:
                            print(f"selamat {username} anda membeli tiket pada hari {hari}")
                            break
                        else:
                            print("uang anda tidak cukup")
                            break
                    else:
                        if hari == "minggu":
                            uang = int(input())
                            hargatiket = 60000
                            if uang >= hargatiket:
                                print(f"selamat {username} anda membeli tiket pada hari {hari}")
                                break
                            else:
                                print("uang anda tidak cukup")
                                break
                        else:
                            print("tidak valid")
        else:
            print("Program Anda Telah Selesai")
    else:
        lanjut = input("Apa Anda Ingin Mengakhiri? (iya/tidak) : ")
        if lanjut == "iya":
            print("program di hentikan")
        else:
            loop = loop + 1
            perulangan = 3 - loop
            print(f"Perulangan sisa {perulangan}")