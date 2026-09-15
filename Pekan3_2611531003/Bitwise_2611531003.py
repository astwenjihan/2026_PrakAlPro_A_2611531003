# Buat file dengan nama Bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: a_1234
# Progran ini menggunakan fungsi input() 

print("\n===================================")
print("3. OPERATOR BITWISE")
print("===================================")

angka1_1003 = int(input("Input angka bitwise-1: "))
angka2_1003 = int(input("Input angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("Angka1 =", angka1_1003, "dalam biner =", bin(angka1_1003))
print("Angka2 =", angka2_1003, "dalam biner =", bin(angka2_1003))

# Bitwise AND
hasil_bitwise_and_1003 = angka1_1003 & angka2_1003
print("\nBitwise AND (&)")
print(angka1_1003, "&", angka2_1003, "=", hasil_bitwise_and_1003)
print("Biner hasil =", bin(hasil_bitwise_and_1003))
print("Biner hasil (8 bit) =", format(hasil_bitwise_and_1003, '08b'))

# Bitwise OR
hasil_bitwise_or_1003 = angka1_1003 | angka2_1003
print("\nBitwise OR (|)")
print(angka1_1003, "|", angka2_1003, "=", hasil_bitwise_or_1003)
print("Biner hasil =", bin(hasil_bitwise_or_1003))
print("Biner hasil (8 bit) =", format(hasil_bitwise_or_1003, '08b'))

# Bitwise XOR
hasil_bitwise_xor_1003 = angka1_1003 ^ angka2_1003
print("\nBitwise XOR (^)")
print(angka1_1003, "^", angka2_1003, "=", hasil_bitwise_xor_1003)
print("Biner hasil =", bin(hasil_bitwise_xor_1003))
print("Biner hasil (8 bit) =", format(hasil_bitwise_xor_1003, '08b'))

# Bitwise NOT
hasil_bitwise_not_1_1003 = ~angka1_1003
print("\nBitwise NOT (~) untuk angka1")
print("~", angka1_1003, "=", hasil_bitwise_not_1_1003)   
print("Biner hasil =", bin(hasil_bitwise_not_1_1003))
print("Biner hasil (8 bit) =", format(hasil_bitwise_not_1_1003, '08b'))                       

# Bitwise geser kiri
jumlah_geser_1003 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_bitwise_shift_left_1003 = angka1_1003 << jumlah_geser_1003
print("\nBitwise geser kiri (<<)")
print(angka1_1003, "<<", jumlah_geser_1003, "=", hasil_bitwise_shift_left_1003)
print("Biner hasil =", bin(hasil_bitwise_shift_left_1003))
print("Biner hasil (8 bit) =", format(hasil_bitwise_shift_left_1003, '08b'))

# Bitwise geser kanan
hasil_bitwise_shift_right_1003 = angka1_1003 >> jumlah_geser_1003
print("\nBitwise geser kanan (>>)")
print(angka1_1003, ">>", jumlah_geser_1003, "=", hasil_bitwise_shift_right_1003)
print("Biner hasil =", bin(hasil_bitwise_shift_right_1003))
print("Biner hasil (8 bit) =", format(hasil_bitwise_shift_right_1003, '08b'))