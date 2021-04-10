print("Selamat datang di Cahaya Travel".center(75, "="))
menu = """
|1| Paket 2D1N Bali
|2| Paket 2D1N Lombok
|3| Paket 3D1N Lombok
[q] Keluar aplikasi
"""

while True:
    print(menu)
    choice = input("Masukkan nomor menu : ")

    if choice     == '1':
        paket     = "Paket 2D1N Bali"
        destinasi = "Tujuan Wisata: Uluwatu, Dreamland, Garuda Wisnu Kencana"
        harga     = 800000

    elif choice   == '2':
        paket     = "Paket 2D1N Lombok"
        destinasi = "Tujuan Wisata: Desa Sasak, Narmada, Batu Bolong"
        harga     = 1100000

    elif choice   == '3':
        paket     = "Paket 3D1N Lombok"
        destinasi = "Tujuan Wisata: Gili Trawangan, Gili Air, Gili Nemo"
        harga     = 2000000

    elif choice   == 'q':
        print("Terima kasih sudah mengunjungi Cahaya Travel")
        break

    else:
        print("Maaf, paket tidak tersedia.")
        continue

    print(f"Paket pilihan       : {paket}")
    print(f"Destinasi wisata    : {destinasi}")
    print(f"Harga               : Rp. {harga}")