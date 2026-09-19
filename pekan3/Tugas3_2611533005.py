print("======================================")
print("          SISTEM TRANSAKSI TOKO       ")
print("======================================")

nama_3005 = input("\nMasukkan Nama Pelanggan : ")
status_3005 = input("Masukkan Status Pelanggan (member/nonmember) : ")
total_belanja_3005 = float(input("Masukkan Total Belanja : Rp "))
jumlah_barang_3005 = int(input("Masukkan Jumlah Barang : "))
kode_promo_3005 = input("Masukkan Kode Promo : ")

syarat_belanja_3005 = total_belanja_3005 >= 200000
syarat_barang_3005 = jumlah_barang_3005 >= 3
status_member_3005 = status_3005 == "member"

daftar_promo_3005 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

kode_tersedia_3005 = kode_promo_3005 in daftar_promo_3005
kode_tidak_tersedia_3005 = kode_promo_3005 not in daftar_promo_3005

diskon_member_3005 = status_member_3005 and syarat_belanja_3005
dapat_promo_3005 = syarat_barang_3005 and kode_tersedia_3005

akses_umum_3005 = status_member_3005 or kode_tersedia_3005
bukan_member_3005 = not status_member_3005

if diskon_member_3005:
    diskon_3005 = total_belanja_3005 * 10 / 100
else:
    diskon_3005 = 0

total_pembayaran_3005 = total_belanja_3005 - diskon_3005

if jumlah_barang_3005 != 0:
    rata_rata_3005 = total_belanja_3005 / jumlah_barang_3005
else:
    rata_rata_3005 = 0

sisa_bagi_3005 = total_belanja_3005 % jumlah_barang_3005

total_setelah_tambahan_3005 = total_pembayaran_3005
total_setelah_tambahan_3005 += 0

objek1_3005 = daftar_promo_3005
objek2_3005 = daftar_promo_3005.copy()

identitas_sama_3005 = objek1_3005 is objek2_3005
identitas_berbeda_3005 = objek1_3005 is not objek2_3005

kode_member_3005 = 1
kode_belanja_3005 = 2
kode_barang_3005 = 4
kode_promo_bit_3005 = 8

kode_status_3005 = 0

if status_member_3005:
    kode_status_3005 = kode_status_3005 | kode_member_3005

if syarat_belanja_3005:
    kode_status_3005 = kode_status_3005 | kode_belanja_3005

if syarat_barang_3005:
    kode_status_3005 = kode_status_3005 | kode_barang_3005

if kode_tersedia_3005:
    kode_status_3005 = kode_status_3005 | kode_promo_bit_3005

cek_member_3005 = kode_status_3005 & kode_member_3005
cek_promo_3005 = kode_status_3005 & kode_promo_bit_3005

kode_referensi_3005 = 11
hasil_xor_3005 = kode_status_3005 ^ kode_referensi_3005

hasil_shift_3005 = kode_status_3005 << 1

member_access_3005 = cek_member_3005 == 1
promo_access_3005 = cek_promo_3005 == 8
free_shipping_access_3005 = kode_promo_3005 == "GRATISONGKIR"

print("\n======================================")
print("             DATA TRANSAKSI           ")
print("======================================")
print("Nama Pelanggan       :", nama_3005)
print("Status Pelanggan     :", status_3005)
print("Total Belanja        : Rp", int(total_belanja_3005))
print("Jumlah Barang        :", jumlah_barang_3005)
print("Kode Promo           :", kode_promo_3005)

print("\n======================================")
print("             HASIL VALIDASI           ")
print("======================================")
print("Belanja >= Rp200000       :", syarat_belanja_3005)
print("Jumlah Barang >= 3        :", syarat_barang_3005)
print("Status Member             :", status_member_3005)
print("Kode Promo Tersedia       :", kode_tersedia_3005)
print("Mendapatkan Diskon        :", diskon_member_3005)
print("Mendapatkan Promo         :", dapat_promo_3005)

print("\n======================================")
print("           HASIL PERHITUNGAN          ")
print("======================================")
print("Diskon                    : Rp", int(diskon_3005))
print("Total Pembayaran          : Rp", int(total_pembayaran_3005))
print("Rata-rata Harga Barang    : Rp", int(rata_rata_3005))

print("\n======================================")
print("          HAK AKSES PELANGGAN         ")
print("======================================")
print("Kode Hak Akses            :", kode_status_3005)
print("Member Access             :", member_access_3005)
print("Promo Access              :", promo_access_3005)
print("Free Shipping Access      :", free_shipping_access_3005)

print("\n======================================")
print("             OPERASI BITWISE          ")
print("======================================")

print("          Kode Status Transaksi       ")
print("0001 | 0010 | 0100 | 1000")
print("Kode Biner   :", format(kode_status_3005, "04b"))
print("Kode Desimal :", kode_status_3005)

print("\n==========Pemeriksaan Status==========")

print("\nCek Member")
print(format(kode_status_3005, "04b"), "&", format(kode_member_3005, "04b"))
print("Hasil Biner   :", format(cek_member_3005, "04b"))
print("Hasil Desimal :", cek_member_3005)

print("\nCek Promo")
print(format(kode_status_3005, "04b"), "&", format(kode_promo_bit_3005, "04b"))
print("Hasil Biner   :", format(cek_promo_3005, "04b"))
print("Hasil Desimal :", cek_promo_3005)

print("\n==========Perbandingan Status==========")
print("Kode Transaksi :", format(kode_status_3005, "04b"))
print("Kode Referensi :", format(kode_referensi_3005, "04b"))
print(format(kode_status_3005, "04b"), "^", format(kode_referensi_3005, "04b"))
print("Hasil Biner   :", format(hasil_xor_3005, "04b"))
print("Hasil Desimal :", hasil_xor_3005)

print("\n==========Shift==========")
print(format(kode_status_3005, "04b"), "<< 1")
print("Hasil Biner   :", format(hasil_shift_3005, "05b"))
print("Hasil Desimal :", hasil_shift_3005)

print("\n======================================")
print("                SELESAI               ")
print("======================================")