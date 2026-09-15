# Buat file dengan nama Boolean_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: nama_1234
# Deklarasi variabel dengan tipe data Boolean
is_lulus_1003 = True
is_cumlaude_1003 = True

# Menggunakan Boolean
nilai_1003 = 85
batas_lulus_1003 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan_1003 = nilai_1003 >= batas_lulus_1003 # Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai:", nilai_1003)
print("Apakah lulus?", status_kelulusan_1003)
if is_lulus_1003 and is_cumlaude_1003:
    print("Selamat, Anda lulus dengan predikat Cumlaude!")