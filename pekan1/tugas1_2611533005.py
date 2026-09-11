print("=== PROGRAM DISKON ===")
harga = float(input("Masukkan harga barang: Rp "))
diskon = float(input("Masukkan diskon (%): "))

potongan = harga * diskon / 100
harga_akhir = harga - potongan

print("\n=== HASIL ===")
print("Harga awal   : Rp", harga)
print("Potongan     : Rp", potongan)
print("Harga akhir  : Rp", harga_akhir)