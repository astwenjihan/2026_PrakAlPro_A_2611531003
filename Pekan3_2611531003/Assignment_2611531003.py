# Buat file dengan nama Assignment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: a_1234
# Progran ini menggunakan fungsi input() 
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam Python

angka1_1003 = int(input("Input angka-1: "))
angka2_1003 = int(input("Input angka-2: "))

print("\nnilai awal angka1 =", angka1_1003)
print("nilai awal angka2 =", angka2_1003)

# Assignment biasa
hasil_assignment_biasa_1003 = angka1_1003
print("\nAssignment biasa (=)")
print("Hasil =", hasil_assignment_biasa_1003)

# Assignment penambahan
hasil_assignment_penambahan_1003 = angka1_1003 
hasil_assignment_penambahan_1003 += angka2_1003
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil_assignment_penambahan_1003)

# Assignment pengurangan
hasil_assignment_pengurangan_1003 = angka1_1003
hasil_assignment_pengurangan_1003 -= angka2_1003
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil_assignment_pengurangan_1003)

# Assignment perkalian
hasil_assignment_perkalian_1003 = angka1_1003
hasil_assignment_perkalian_1003 *= angka2_1003
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil_assignment_perkalian_1003)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_1003 != 0:
    hasil_assignment_pembagian_1003 = angka1_1003
    hasil_assignment_pembagian_1003 /= angka2_1003
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil_assignment_pembagian_1003)
    # Operator tambahan
    hasil_assignment_pembagian_bulat_1003 = angka1_1003
    hasil_assignment_pembagian_bulat_1003 //= angka2_1003
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil_assignment_pembagian_bulat_1003)
    hasil_assignment_sisa_bagi_1003 = angka1_1003
    hasil_assignment_sisa_bagi_1003 %= angka2_1003
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil_assignment_sisa_bagi_1003)
else:
    print("\nPembagian tidak dapat dilakukan")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: Assignment perpangkatan
hasil_assignment_perpangkatan_1003 = angka1_1003
hasil_assignment_perpangkatan_1003 **= angka2_1003
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil_assignment_perpangkatan_1003)