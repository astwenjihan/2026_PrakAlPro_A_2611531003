print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

n_1003 = int(input("Masukkan ukuran skala jam pasir (N): "))

print("#", end="")
for i_1003 in range(4 * n_1003 + 5):
    print("=", end="")
print("#")

for baris_1003 in range(n_1003, 0, -1):
    print("| ", end="")

    for spasi_1003 in range(2 * (n_1003 - baris_1003)):
        print(" ", end="")

    for angka_1003 in range(baris_1003, 0, -1):
        print(angka_1003, end="")
        if angka_1003 > 1:
            print(" ", end="")

    print("<*>", end="")

    for angka_1003 in range(1, baris_1003 + 1):
        print(" ", end="")
        print(angka_1003, end="")

    for spasi_1003 in range(2 * (n_1003 - baris_1003)):
        print(" ", end="")

    print(" |")

print("|", end="")
for spasi_1003 in range(2 * n_1003 + 1):
    print(" ", end="")

print("<*>", end="")

for spasi_1003 in range(2 * n_1003 + 1):
    print(" ", end="")

print(
    "|")

for baris_1003 in range(1, n_1003 + 1):
    print("| ", end="")

    for spasi_1003 in range(2 * (n_1003 - baris_1003)):
        print(" ", end="")

    for angka_1003 in range(baris_1003, 0, -1):
        print(angka_1003, end="")
        if angka_1003 > 1:
            print(" ", end="")

    print("<*>", end="")

    for angka_1003 in range(1, baris_1003 + 1):
        print(" ", end="")
        print(angka_1003, end="")

    for spasi_1003 in range(2 * (n_1003 - baris_1003)):
        print(" ", end="")

    print(" |")

print("#", end="")
for i_1003 in range(4 * n_1003 + 5):
    print("=", end="")
print("#")