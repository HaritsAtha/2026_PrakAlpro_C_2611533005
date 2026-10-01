# Buat file dengan nama nested_for3_NIM.py
# Buat program untuk perulangan dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_3005 = int(input("Masukkan nilai batas: "))
for i_3005 in range(batas_3005 + 1):
    for j_3005 in range(batas_3005+1):
        print(i_3005+j_3005, end=" ")
    print() # pindah ke baris berikutnya