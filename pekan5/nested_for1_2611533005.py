# Buat file dengan nama nested_for1_NIM.py
# Buat program untuk perulangan dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_3005 = int(input("Masukkan nilai batas: "))
for line_3005 in range(1, batas_3005 + 1):
    for j_3005 in range(1, (-1 * line_3005 + batas_3005) + 1):
        print(".", end=" ")
    print(line_3005)