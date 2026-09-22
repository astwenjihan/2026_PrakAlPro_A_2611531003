# Input dari user
total_belanja_1003 = float(input("Masukkan total belanja (Rp): "))

# Input dari status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_1003 = input("Apakah anda member (y/t): ").strip().lower()
is_member_1003 = input_member_1003 in ['y', 'ya']

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya') 
input_promo_1003 = input("Apakah kode promo valid? (y/t):").strip().lower() 
kode_promo_valid_1003 = input_promo_1003 in["y", "ya"]

total_diskon_persen_1003 = 0

if total_belanja_1003 > 10000000: 
    total_diskon_persen_1003 +=10 #Diskon belanja besar

if is_member_1003:
    total_diskon_persen_1003 += 5 #Diskon member

if kode_promo_valid_1003: 
    total_diskon_persen_1003 +=15 #Diskon voucher

#Menghitung nominal diskon dan total bayar
nominal_diskon_1003 = total_belanja_1003 * (total_diskon_persen_1003 / 100) 
total_bayar_1003 = total_belanja_1003 - nominal_diskon_1003

#Output hasil
print("/n--- Rincian Pembayaran ---")
print(f"Total Diskon : {total_diskon_persen_1003}%(Rp{nominal_diskon_1003:,.0f})")
print(f"Total Bayar: Rp {total_bayar_1003:,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_persen_1003}%")
# Output total diskon yang anda dapatkan: 30% jika belanja > 1juta, member, dan kode promo valid