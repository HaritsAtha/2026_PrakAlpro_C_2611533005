# Buat file dengan nama Boolean_NIM.py
# Nama variable dtambah 4 digit terakhir contoh: nilai_1234
# Deklarasi variable dengan tipe data boolean
# # Deklarasi variabel dengan tipe data Boolean
is_lulus_3005 = True
is_cumlaude_3005 = True

# Menggunakan Boolean
nilai_3005 = 85
batas_lulus_3005 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan_3005 = nilai_3005 >= batas_lulus_3005 # Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai:", nilai_3005)
print("Apakah Lulus?:", status_kelulusan_3005)
if is_lulus_3005 and is_cumlaude_3005:
    print("Selamat, Anda lulus dengan predikat Cumlaude!")