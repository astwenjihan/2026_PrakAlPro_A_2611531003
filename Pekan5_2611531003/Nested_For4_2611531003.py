# Buat file dnegan nama Nested_For4_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama Variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_1003 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_1003 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_1003 = tinggi_1003
    c_1003 = a_1003
    lebar_1003 = (2 * tinggi_1003) - 2

    for i in range(1, tinggi_1003 + 1):
        b_1003 = c_1003 + 1

        for j in range (1, lebar_1003 + 1):

            # Baris atas dan bawah
            if i == 1 or i == tinggi_1003:
                if j == 1 or j == lebar_1003:
                    print("#", end="")
                else:
                    print("=", end="")

            # Baris isi
            else:
                if j == 1 or j == lebar_1003:
                    print("|", end="")
                else: 
                    if j == c_1003:
                        print("<", end="")
                    elif j == b_1003:
                        print(">", end="")
                    elif j == (lebar_1003 - c_1003):
                        print("<", end="")
                    elif j == (lebar_1003 - c_1003 + 1):
                        print(">", end="")
                    elif j > b_1003 and j < (lebar_1003 - c_1003):
                        print(".", end="")
                    else:
                        print(" ", end="")
        print()

        # logika asli java
        a_1003 -= 2

        if a_1003 <= 0:
            c_1003 = (-a_1003) + 2
        else:
            c_1003 = a_1003