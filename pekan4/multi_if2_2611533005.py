# Buat file dengan nama multi_if2_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: total_belanja_1234
# Program ini menggunakan fungsi input()
# Program menghitung diskon belanja

# Input dari user
total_belanja_3005 = float(input("Masukkan total belanja (Rp): "))

# Input status mnember (mengecek apakah user mengetik 'y' atau 'ya')
input_member__3005 = input("Apakah Anda member? (y/t): ").strip().lower()
is_member_3005 = input_member__3005 in ["y", "ya"] 

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_3005 = input("Apakah kode promo valid? (y/t) : ").strip().lower()
kode_promo_valid_3005 = input_promo_3005 in ["y", "ya"]

total_diskon_persen_3005 = 0

# Multi-IF terpisah: Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus\

if total_belanja_3005 > 1000000:
    total_diskon_persen_3005 += 10 # Diskon belanja besar

if is_member_3005:
    total_diskon_persen_3005 += 5 # Diskon member

if kode_promo_valid_3005:
    total_diskon_persen_3005 += 15 # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_3005 = total_belanja_3005 * (total_diskon_persen_3005 / 100)
total_bayar_3005 = total_belanja_3005 - nominal_diskon_3005

# Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total DIskon : {total_diskon_persen_3005}% (Rp {nominal_diskon_3005:,.0f})")
print(f"Total Bayar  : Rp {total_bayar_3005:,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_persen_3005}%")
# Output : total diskon yang anda dapatkan: 30% jika belanja . 1 juta, member, dan kode promo valid