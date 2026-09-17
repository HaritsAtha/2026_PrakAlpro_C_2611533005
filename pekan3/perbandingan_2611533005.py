# Buat file dengan nama perbandingan_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator pebandingan dalam Python

angka1_3005 = int(input("Input angka-1: "))
angka2_3005 = int(input("Input angka-2: "))

# Lebih besar dari
hasil_3005 = angka1_3005 > angka2_3005
print("\nOperator lebih besar dari")
print("angka1_3005 > angka2_3005 = ", hasil_3005)

# Lebih kecil dari
hasil_3005 = angka1_3005 < angka2_3005
print("\nOperator lebih kecil dari")
print("angka1_3005 < angka2_3005 =", hasil_3005)

# Lebih besar dari atau sama dengan
hasil_3005 = angka1_3005 >= angka2_3005
print("\nOperator lebih besar dari atau sama dengan")
print("angka1_3005 >= angka2_3005 =", hasil_3005)

# Lebih kecil dari atau sama dengan
hasil_3005 = angka1_3005 <= angka2_3005
print("\nOperator lebih kecil dari atau sama dengan")
print("angka1_3005 <= angka2_3005 =", hasil_3005)

# Sama dengan
hasil_3005 = angka1_3005 == angka2_3005
print("\nOperator sama dengan")
print("angka1_3005 == angka2_3005 =", hasil_3005)

# Tidak sama dengan
hasil_3005 = angka1_3005 != angka2_3005
print("\nOperator tidak sama dengan")
print("angka1_3005 != angka2_3005 =", hasil_3005)

# Tambahan: perbandingan berantai dalam Python
hasil = 0 < angka1_3005 < 100
print("\nPerbandingan berantai")
print("0 < angka1_3005 < 100 =", hasil)

hasil = 0 < angka2_3005 < 100
print("0 < angka2_3005 < 100 =", hasil)