# Buat file dengan nama if2_NIM.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

ipk_3005 = float(input("Input IPK Anda = "))

if ipk_3005 > 2.75:
    print("Anda Lulus Sangat Memuaskan dengan IPK " + str(ipk_3005))
else:
    print("Anda Tidak Lulus")
print("Program Selesai")