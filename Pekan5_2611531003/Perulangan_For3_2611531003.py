# Buat file dnegan nama Perulangan_For3_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama Variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_1003 = int(input("Masukkan jumlah perulangan: "))

jumlah_1003 = 0
for i in range(1, ulang_1003 + 1):
    print(i, end=" ")
    jumlah_1003 = jumlah_1003 + i

    if i < ulang_1003:
        print(" + ", end="")
    else:
        print(" = ", jumlah_1003, end="")
print()
print("Jumlah =", jumlah_1003)