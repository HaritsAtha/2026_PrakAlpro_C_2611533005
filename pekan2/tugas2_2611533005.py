from typing import Final

BATAS_LULUS: Final = 75.0

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

nama_3005 = input("Masukkan Nama Mahasiswa : ")
jenis_kelamin_3005 = input("Masukkan Jenis Kelamin (L/P): ")
umur_3005 = int(input("Masukkan Umur : "))
nilai_3005 = float(input("Masukkan Skor Tes Awal : "))

alamat_3005 = """Komplek Unand,
Kecamatan Pauh,
Kota Padang"""

id_token_3005 = 100 + 3j

lulus_3005 = nilai_3005 >= BATAS_LULUS

print()
print("=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa :", nama_3005, "| Tipe:", type(nama_3005))
print("Jenis Kelamin :", jenis_kelamin_3005, "| Tipe:", type(jenis_kelamin_3005))
print("Alamat Domisili:")
print(alamat_3005, "| Tipe:", type(alamat_3005))
print("Umur :", umur_3005, "tahun | Tipe:", type(umur_3005))
print("Skor Tes Awal :", nilai_3005, "| Tipe:", type(nilai_3005))
print("ID Token Sinyal:", id_token_3005, "| Tipe:", type(id_token_3005))

print()
print("=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai:", BATAS_LULUS)
print("Apakah Dinyatakan Lulus?:", lulus_3005, "| Tipe:", type(lulus_3005))