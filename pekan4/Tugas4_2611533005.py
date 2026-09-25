print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

nama_3005 = input("Masukkan Nama Pengunjung        : ")
umur_3005 = int(input("Input umur anda                 : "))
sim_3005 = input("Apakah Anda Sudah Punya SIM C (y/t): ")[0].lower()

print("\nPilihan Paket Wahana (1-5):")
print(" 1. Safari Rimba         (Rp 50,000)")
print(" 2. Arung Jeram          (Rp 75,000)")
print(" 3. Motor ATV Ekstrim    (Rp 120,000)")
print(" 4. Roller Coaster Kilat (Rp 100,000)")
print(" 5. All-Access VIP       (Rp 220,000)")

paket_3005 = int(input("Masukkan nomor paket (1-5)      : "))
jumlah_tiket_3005 = int(input("Masukkan jumlah tiket           : "))

if jumlah_tiket_3005 <= 0:
    print("Peringatan: Kuota tiket tidak valid.")

match paket_3005:
    case 1:
        harga_3005 = 50000
    case 2:
        harga_3005 = 75000
    case 3:
        harga_3005 = 120000
    case 4:
        harga_3005 = 100000
    case 5:
        harga_3005 = 220000
    case _:
        print("Paket wahana tidak valid!")
        exit()

member_3005 = input("Apakah Anda member? (y/t)       : ").strip().lower()
promo_3005 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()

print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

if paket_3005 == 3 and umur_3005 >= 17 and sim_3005 == "y":
    print("Status Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
elif paket_3005 == 3 and umur_3005 >= 17 and sim_3005 != "y":
    print("Status Akses: Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
elif paket_3005 == 3 and umur_3005 < 17 and sim_3005 == "y":
    print("Status Akses: Identitas tidak valid: Belum cukup umur memiliki SIM.")
elif paket_3005 == 3:
    print("Status Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV.")
elif umur_3005 >= 10:
    print("Status Akses: Anda memenuhi syarat umur.")
else:
    print("Status Akses: Anda belum cukup umur.")

subtotal_3005 = harga_3005 * jumlah_tiket_3005
total_diskon_persen_3005 = 0

if subtotal_3005 >= 200000:
    total_diskon_persen_3005 += 10
if member_3005 in ["y", "ya"]:
    total_diskon_persen_3005 += 5
if promo_3005 in ["y", "ya"]:
    total_diskon_persen_3005 += 15
if jumlah_tiket_3005 >= 5:
    total_diskon_persen_3005 += 5

nominal_diskon_3005 = subtotal_3005 * (total_diskon_persen_3005 / 100)
total_bayar_3005 = subtotal_3005 - nominal_diskon_3005

if total_bayar_3005 > 300000:
    catatan_3005 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    catatan_3005 = "Terima kasih telah berkunjung."

print("\n--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {subtotal_3005:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_3005}% (Rp {nominal_diskon_3005:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_3005:,.0f}")
print(f"Catatan Layanan  : {catatan_3005}")
print("Program Selesai")