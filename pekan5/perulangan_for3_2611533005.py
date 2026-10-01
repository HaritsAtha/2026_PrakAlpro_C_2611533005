# Buat file dengan nama perulangan_for3_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_3005 = int(input("Masukkan jumlah perulangan : "))

jumlah_3005 = 0
for i_3005 in range(1, ulang_3005 + 1):
    print(i_3005, end=" ")
    jumlah_3005 = jumlah_3005 + i_3005

    if i_3005 < ulang_3005:
        print(" + ", end="")
    else:
        print(" = ", jumlah_3005, end="")
print()
print("Jumlah =", jumlah_3005)