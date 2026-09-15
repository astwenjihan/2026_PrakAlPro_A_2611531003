# Buat file dengan nama Perbandingan_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: a_1234
# Progran ini menggunakan fungsi input() 
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam Python

angka1_1003 = int(input("Input angka-1: "))
angka2_1003 = int(input("Input angka-2: "))

# Lebih besar dari
hasil_lebih_besar_1003 = angka1_1003 > angka2_1003
print("\nOperator Lebih besar dari")
print("angka1 > angka2 =", hasil_lebih_besar_1003)

# Lebih kecil dari
hasil_lebih_kecil_1003 = angka1_1003 < angka2_1003
print("\nOperator Lebih kecil dari")
print("angka1 < angka2 =", hasil_lebih_kecil_1003)

# Lebih besar dari atau sama dengan
hasil_lebih_besar_sama_1003 = angka1_1003 >= angka2_1003
print("\nOperator Lebih besar dari atau sama dengan")
print("angka1 >= angka2 =", hasil_lebih_besar_sama_1003)

# Lebih kecil dari atau sama dengan
hasil_lebih_kecil_sama_1003 = angka1_1003 <= angka2_1003
print("\nOperator Lebih kecil dari atau sama dengan")
print("angka1 <= angka2 =", hasil_lebih_kecil_sama_1003)

# Sama dengan
hasil_sama_dengan_1003 = angka1_1003 == angka2_1003
print("\nOperator Sama dengan")
print("angka1 == angka2 =", hasil_sama_dengan_1003)

# Tidak sama dengan
hasil_tidak_sama_dengan_1003 = angka1_1003 != angka2_1003
print("\nOperator Tidak sama dengan")
print("angka1 != angka2 =", hasil_tidak_sama_dengan_1003)

# Tambahan: Perbandingan berantai dalam Python
hasil_perbandingan_berantai_1003 = 0 < angka1_1003 < 100
print("\nPerbandingan berantai")
print("0 < angka1 < 100 =", hasil_perbandingan_berantai_1003)

hasil_perbandingan_berantai_2_1003 = 0 < angka2_1003 < 100
print("0 < angka2 < 100 =", hasil_perbandingan_berantai_2_1003)