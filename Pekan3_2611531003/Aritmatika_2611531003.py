# Buat file dengan nama Aritmatika_NIM.py
# Buat program untuk operator aritmatika dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: a_1234
# Program ini menggunakan fungsi input() 
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_1003 = int(input("Input angka-1: "))
angka2_1003 = int(input("Input angka-2: "))

# Penjumlahan
hasil_penjumlahan_1003 = angka1_1003 + angka2_1003
print("\n0perator Penjumlahan")
print("Hasil =", hasil_penjumlahan_1003)

# Pengurangan
hasil_pengurangan_1003 = angka1_1003 - angka2_1003
print("\nOperator Pengurangan")
print("Hasil =", hasil_pengurangan_1003)

# Perkalian
hasil_perkalian_1003 = angka1_1003 * angka2_1003
print("\nOperator Perkalian")
print("Hasil =", hasil_perkalian_1003)

# Pembagian, Pembagian Bulat, dan sisa bagi
if angka2_1003 != 0:
    hasil_pembagian_1003 = angka1_1003 / angka2_1003
    print("\nOperator Pembagian")
    print("Hasil =", hasil_pembagian_1003)

    hasil_pembagian_bulat_1003 = angka1_1003 // angka2_1003
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_pembagian_bulat_1003)

    hasil_sisa_bagi_1003 = angka1_1003 % angka2_1003
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_sisa_bagi_1003)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_pangkat_1003 = angka1_1003 ** angka2_1003
print("\nOperator Pangkat")
print("Hasil =", hasil_pangkat_1003)