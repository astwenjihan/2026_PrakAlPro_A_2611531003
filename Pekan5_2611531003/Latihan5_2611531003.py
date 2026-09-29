tinggi_1003 = int(input("Masukkan tinggi segitiga: "))

for i in range(1, tinggi_1003 + 1):
    print(" " * (tinggi_1003 - i), end="")

    print("* " * i)