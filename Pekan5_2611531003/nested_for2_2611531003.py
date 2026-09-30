# Buat file dnegan nama Nested_For2_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama Variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_1003 = int(input("Masukkan nila batas: "))
for i in range(1, batas_1003 + 1):
    for j in range(1, batas_1003 + 1):
        print("+", end="")
    print() # Pindah ke baris berikutnya