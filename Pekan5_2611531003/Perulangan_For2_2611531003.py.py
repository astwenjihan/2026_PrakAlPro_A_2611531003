# Buat file dnegan nama Perulangan_For2_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama Variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_1003 = int(input("Masukkan jumlah perulangan: "))
print("Perulangan ke-0 sampai ke-", ulang_1003-1)
for i in range(ulang_1003):
    print(i, end=" ")
print()
print("Perulagan ke-1 sampai ke-", ulang_1003)
for i in range(1, ulang_1003+1):
    print(i, end=" ")