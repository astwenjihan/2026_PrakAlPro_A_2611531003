# 1. Konstanta Batas Kelulusan
# Nama variabel ditambah 4 digit nim terakhir contoh: a_1234
Batas_Lulus_1003 = 75.0

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

# 2. Input Data (String & Numerik)
nama_1003 = input("Masukkan Nama Mahasiswa : ")
jk_1003 = input("Masukkan Jenis Kelamin (L/P): ")

# Alamat menggunakan petik tiga (multiline) sesuai ketentuan tugas
alamat_1003 = """Jl. Kampus Unand,
Kecamatan Pauh,
Kota Padang"""

umur_1003 = int(input("Masukkan Umur : "))
nilai_1003 = float(input("Masukkan Skor Tes Awal : "))

# Variabel bilangan kompleks untuk token (tipe data complex)
token_1003 = 100 + 3j

# 3. Evaluasi Boolean (Status Kelulusan)
status_lulus_1003 = nilai_1003 >= Batas_Lulus_1003

# 4. Output dan Pengecekan Tipe Data dengan type()
print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print(f"Nama Mahasiswa : {nama_1003} | Tipe: {type(nama_1003)}")
print(f"Jenis Kelamin : {jk_1003} | Tipe: {type(jk_1003)}")
print(f"Alamat Domisili:\n{alamat_1003} | Tipe: {type(alamat_1003)}")
print(f"Umur : {umur_1003} tahun | Tipe: {type(umur_1003)}")
print(f"Skor Tes Awal : {nilai_1003} | Tipe: {type(nilai_1003)}")
print(f"ID Token Sinyal: {token_1003} | Tipe: {type(token_1003)}")

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print(f"Batas Minimum Nilai: {Batas_Lulus_1003}")
print(f"Apakah Dinyatakan Lulus?: {status_lulus_1003} | Tipe: {type(status_lulus_1003)}")