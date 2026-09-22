# Program Studi Kasus: Sistem Loket Terpadu & Audit Transaksi Ekspedisi Wahana
# Nama File: tugas4_2611531003.py

print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

#1 Input Data Pengunjung & String Handling
nama_pengunjung_1003 = input("Masukkan nama pengunjung: ")
umur_pengunjung_1003 = int(input("Input umur anda: "))
sim_input_1003 = input("Apakah anda memiliki SIM-C? (y/t): ")
sim_pengunjung_1003 = sim_input_1003.strip().lower()[0] if sim_input_1003 else 't'
jumlah_tiket_1003 = int(input("Masukkan jumlah tiket  : "))

# Penerapan IF Tunggal untuk validasi kuota tiket
if jumlah_tiket_1003 <= 0:
    print("\nPeringatan: Kuota tiket tidak valid!")

# Tampilan Menu Wahana
print("\nPilihan Paket Wahana (1-5):")
print("1. Safari Rimba         (Rp 50,000)")
print("2. Arung Jeram          (Rp 75,000)")
print("3. Motor ATV Ekstrim    (Rp 120,000)")
print("4. Roller Coaster Kilat (Rp 100,000)")
print("5. All-Access VIP       (Rp 220,000)")

paket_1003 = int(input("Masukkan nomor paket (1-5) : "))

# 2. Pemilihan Wahana Menggunakan match - case
is_valid_paket_1003 = True
nama_wahana_1003 = ""
harga_satuan_1003 = 0

match paket_1003:
    case 1:
        nama_wahana_1003 = "Wahana Safari Rimba"
        harga_satuan_1003 = 50000
    case 2:
        nama_wahana_1003 = "Wahana Arung Jeram"
        harga_satuan_1003 = 75000
    case 3:
        nama_wahana_1003 = "Wahana Motor ATV Ekstrim"
        harga_satuan_1003 = 120000
    case 4:
        nama_wahana_1003 = "Wahana Roller Coaster Kilat"
        harga_satuan_1003 = 100000
    case 5:
        nama_wahana_1003 = "Wahana All-Access VIP"
        harga_satuan_1003 = 220000
    case _:
        print("Paket wahana tidak valid!")
        is_valid_paket_1003 = False

# Memastikan transaksi hanya berlanjut jika paket & tiket valid
if is_valid_paket_1003 and jumlah_tiket_1003 > 0:
    member_input_1003 = input("Apakah Anda member? (y/t) : ")
    is_member_1003 = member_input_1003.strip().lower()[0] if member_input_1003 else 't'

    promo_input_1003 = input("Apakah kode promo valid? (y/t) : ")
    kode_promo_valid_1003 = promo_input_1003.strip().lower()[0] if promo_input_1003 else 't'

    # 3. Validasi Izin Kendali Wahana Menggunakan if - elif - else & Operator Logika
    print("\n--- KELAYAKAN PENGENDARA WAHANA ---")
    if paket_1003 == 3:
        if umur_pengunjung_1003 >= 17 and sim_1003 == 'y':
            print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
        elif umur_pengunjung_1003 >= 17 and sim_1003 != 'y':
            print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
        elif umur_pengunjung_1003 < 17 and sim_1003 == 'y':
            print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
        else:
            print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
    else:
        if umur_pengunjung_1003 >= 10:
            print("Status Akses: Usia memenuhi syarat untuk wahana ini.")
        else:
            print("Status Akses: Pengunjung di bawah umur 10 tahun wajib dalam pengawasan orang tua.")

    # 4. Akumulasi Diskon Bertingkat Menggunakan Multi-IF Terpisah
    subtotal_1003 = harga_satuan_1003 * jumlah_tiket_1003
    total_diskon_persen_1003 = 0

    if subtotal_1003 >= 200000:
        total_diskon_persen_1003 += 10
    if is_member_1003 in ['y', 'ya']:
        total_diskon_persen_1003 += 5
    if kode_promo_valid_1003 in ['y', 'ya']:
        total_diskon_persen_1003 += 15
    if jumlah_tiket_1003 >= 5:
        total_diskon_persen_1003 += 5

    # 5. Evaluasi Kelulusan Audit Menggunakan if - else
    nominal_diskon_1003 = subtotal_1003 * (total_diskon_persen_1003 / 100)
    total_bayar_1003 = subtotal_1003 - nominal_diskon_1003

    print("\n--- Rincian Pembayaran ---")
    print(f"Subtotal Belanja : Rp{int(subtotal_1003):,}".replace(",", "."))
    print(f"Total Diskon     : {total_diskon_persen_1003}% (Rp{int(nominal_diskon_1003):,})".replace(",", "."))
    print(f"Total Bayar      : Rp{int(total_bayar_1003):,}".replace(",", "."))

    if total_bayar_1003 > 300000:
        print("Catatan Layanan  : Selamat! Anda berhak mendapatkan Souvenir Gratis.")
    else:
        print("Catatan Layanan  : Terima kasih telah berkunjung.")

    print("Program Selesai")