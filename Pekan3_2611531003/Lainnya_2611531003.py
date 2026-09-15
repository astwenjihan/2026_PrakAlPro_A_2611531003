# Buat file dengan nama Lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: a_1234
# Progran ini menggunakan fungsi input() 
# Program operator keanggotaan dan identitas

print("==================================")
print("1. OPERATOR KEANGGOTAAN")
print("==================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_1003 = input("Masukkan beberapa data, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_list_1003 = [int(angka.strip()) for angka in input_data_1003.split(",")]

nilai_dicari_1003 = int(input("Masukkan nilai yang ingin dicari: "))

# Operator in
hasil_in_1003 = nilai_dicari_1003 in data_list_1003
print("\nOperator keanggotaan IN")
print(nilai_dicari_1003, "in", data_list_1003, "=", hasil_in_1003)

# Operator not in
hasil_not_in_1003 = nilai_dicari_1003 not in data_list_1003
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_1003, "not in", data_list_1003, "=", hasil_not_in_1003)


print("\n==================================")
print("2. OPERATOR IDENTITAS")
print("==================================")

# Objek1 menggunakan list dari input pengguna
objek1_1003 = data_list_1003

# Objek2 menggunakan list dari input pengguna
objek2_1003 = objek1_1003

# Objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_1003 = data_list_1003.copy()

print("Objek1 =", objek1_1003)
print("Objek2 =", objek2_1003)
print("Objek3 =", objek3_1003)

# Operator is
hasil_is_1003 = objek1_1003 is objek2_1003
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil_is_1003)

# Operator is not
hasil_is_not_1003 = objek1_1003 is not objek3_1003
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil_is_not_1003)

# Perbandingan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =", objek1_1003 is objek3_1003)
print("objek1 == objek3 =", objek1_1003 == objek3_1003)