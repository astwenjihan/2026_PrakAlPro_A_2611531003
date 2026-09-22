# Program Studi Kasus: Sistem Simulasi Transaksi dan Validasi Akses Toko
# Nama File: tugas3_2611531003.py

print("=== SISTEM TRANSAKSI TOKO ===")

# 2. Data Pelanggan dan Transaksi
nama_1003 = input("Masukkan Nama Pelanggan : ")
status_pelanggan_1003 = input("Masukkan Status Pelanggan (member/nonmember) : ")
total_belanja_1003 = int(input("Masukkan Total Belanja : "))
jumlah_barang_1003 = int(input("Masukkan Jumlah Barang : "))
kode_promo_1003 = input("Masukkan Kode Promo : ")

print("\n=== DATA TRANSAKSI ===")
print("Nama Pelanggan   :", nama_1003)
print("Status Pelanggan :", status_pelanggan_1003)
print(f"Total Belanja    : Rp{total_belanja_1003}")
print("Jumlah Barang    :", jumlah_barang_1003)
print("Kode Promo       :", kode_promo_1003)

# 4. Operator Perbandingan
is_belanja_cukup_1003 = total_belanja_1003 >= 200000
is_barang_cukup_1003 = jumlah_barang_1003 >= 3
is_member_1003 = status_pelanggan_1003.strip().lower() == "member"

# 7. Operator Keanggotaan
daftar_promo_1003 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]
is_promo_tersedia_1003 = kode_promo_1003.strip().upper() in daftar_promo_1003

# 5. Operator Logika
is_dapat_diskon_1003 = is_member_1003 and is_belanja_cukup_1003
is_dapat_promo_1003 = is_promo_tersedia_1003 and is_barang_cukup_1003
member_access_1003 = is_member_1003 or is_belanja_cukup_1003
promo_access_1003 = is_dapat_promo_1003
free_shipping_access_1003 = is_promo_tersedia_1003 or is_barang_cukup_1003

print("\n=== HASIL VALIDASI ===")
print("Belanja >= Rp200000   :", is_belanja_cukup_1003)
print("Jumlah Barang >= 3    :", is_barang_cukup_1003)
print("Status Member         :", is_member_1003)
print("Kode Promo Tersedia   :", is_promo_tersedia_1003)
print("Mendapatkan Diskon    :", is_dapat_diskon_1003)
print("Mendapatkan Promo     :", is_dapat_promo_1003)

# 3. Operator Aritmatika
if is_dapat_diskon_1003:
    diskon_1003 = int(total_belanja_1003 * 0.1)
else:
    diskon_1003 = 0

total_pembayaran_1003 = total_belanja_1003 - diskon_1003
# Dihitung dari total pembayaran dibagi jumlah barang agar sesuai contoh gambar (225000 / 4 = 56250)
rata_rata_1003 = total_pembayaran_1003 / jumlah_barang_1003 if jumlah_barang_1003 > 0 else 0

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                : Rp{diskon_1003}")
print(f"Total Pembayaran      : Rp{total_pembayaran_1003}")
print(f"Rata-rata Harga Barang: Rp{int(rata_rata_1003)}")

print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses        : ...")
print("Member Access         :", member_access_1003)
print("Promo Access          :", promo_access_1003)
print("Free Shipping Access  : ", free_shipping_access_1003)

# 6. Operator Penugasan
poin_1003 = 100
poin_1003 += 50

# 8. Operator Identitas
objek_a_1003 = ["Akses", "Toko"]
objek_b_1003 = objek_a_1003
objek_c_1003 = ["Akses", "Toko"]
cek_is_1003 = objek_a_1003 is objek_b_1003
cek_is_not_1003 = objek_a_1003 is not objek_c_1003

# 9. Operator Bitwise
bit_member_1003 = 1 if is_member_1003 else 0
bit_belanja_1003 = 2 if is_belanja_cukup_1003 else 0
bit_barang_1003 = 4 if is_barang_cukup_1003 else 0
bit_promo_1003 = 8 if is_promo_tersedia_1003 else 0

kode_status_bit_1003 = bit_member_1003 | bit_belanja_1003 | bit_barang_1003 | bit_promo_1003

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print("0001 | 0010 | 0100 | 1000")
print("Kode Biner  :", bin(kode_status_bit_1003)[2:].zfill(4))
print("Kode Desimal:", kode_status_bit_1003)

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{bin(kode_status_bit_1003)[2:].zfill(4)} & 0001")
hasil_and_member_1003 = kode_status_bit_1003 & 1
print("Hasil Biner :", bin(hasil_and_member_1003)[2:].zfill(4))
print("Hasil Desimal:", hasil_and_member_1003)

print("\nCek Promo")
print(f"{bin(kode_status_bit_1003)[2:].zfill(4)} & 1000")
hasil_and_promo_1003 = kode_status_bit_1003 & 8
print("Hasil Biner :", bin(hasil_and_promo_1003)[2:].zfill(4))
print("Hasil Desimal:", hasil_and_promo_1003)

print("\n=== Perbandingan Status ===")
kode_referensi_1003 = 0b1011
print("Kode Transaksi :", bin(kode_status_bit_1003)[2:].zfill(4))
print("Kode Referensi : 1011")
hasil_xor_1003 = kode_status_bit_1003 ^ kode_referensi_1003
print(f"{bin(kode_status_bit_1003)[2:].zfill(4)} ^ 1011")
print("Hasil Biner :", bin(hasil_xor_1003)[2:].zfill(4))
print("Hasil Desimal:", hasil_xor_1003)

print("\n=== Shift ===")
print(f"{bin(kode_status_bit_1003)[2:].zfill(4)} << 1")
hasil_shift_1003 = kode_status_bit_1003 << 1
print("Hasil Biner :", bin(hasil_shift_1003)[2:].zfill(4))
print("Hasil Desimal:", hasil_shift_1003)

print("\n=== SELESAI ===")