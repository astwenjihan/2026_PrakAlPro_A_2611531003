# Buat file dengan nama Logika_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: a_1234
# Progran ini menggunakan fungsi input() 
# Program operator logika dalam Python

# Memasukkan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_1003 = input("Input nilai boolean-1 (True/False): ").strip().lower() == "true"
a2_1003 = input("Input nilai boolean-2 (True/False): ").strip().lower() == "true"

print("\nA1 =", a1_1003)
print("A2 =", a2_1003)

# Konjungsi: Bernilai True jika keduanya True
hasil_konjungsi_1003 = a1_1003 and a2_1003
print("\nKonjungsi (AND)")
print("A1 AND A2 =", hasil_konjungsi_1003)

# Disjungsi: Bernilai True jika salah satu atau keduanya True
hasil_disjungsi_1003 = a1_1003 or a2_1003
print("\nDisjungsi (OR)")
print("A1 OR A2 =", hasil_disjungsi_1003)

# Negasi A1: Membalik nilai A1
hasil_negasi_1_1003 = not a1_1003
print("\nNegasi A1 (NOT)")
print("NOT A1 =", hasil_negasi_1_1003)

# Negasi A2: Membalik nilai A2
hasil_negasi_2_1003 = not a2_1003
print("\nNegasi A2 (NOT)")
print("NOT A2 =", hasil_negasi_2_1003)

# XOR: Bernilai True jika kedua nilai berbeda
hasil_XOR_1003 = a1_1003 != a2_1003
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil_XOR_1003)