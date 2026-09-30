# Buat file dnegan nama Nested_For3_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama Variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_1003 = int(input("Masukkan nilai batas: "))
for i in range(batas_1003 + 1):
    for j in range(batas_1003 + 1):
        print(i+j, end=" ")
    print()  # Pindah ke baris berikutnya