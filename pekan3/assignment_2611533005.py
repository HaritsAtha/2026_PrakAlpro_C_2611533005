# Buat file dengan nama assigment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menngunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assigment dalam Python

angka1_3005 = int(input("Input angka-1: "))
angka2_3005 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =",angka1_3005)
print("Nilai angka2 =",angka2_3005)

# Assigment biasa
hasil_3005 = angka1_3005 
print("\nAssigment biasa (=)")
print("Hasil =",hasil_3005)

# Assigment penambahan
hasil_3005 = angka1_3005 
hasil_3005 += angka2_3005 
print("\nAssigment penambahan (+=)")
print("Hasil =",hasil_3005)

# Assigment pengurangan
hasil_3005 = angka1_3005 
hasil_3005 -= angka2_3005 
print("\nAssigment pengurangan (-=)")
print("Hasil =",hasil_3005)

# Assigment perkalian
hasil_3005 = angka1_3005 
hasil_3005 *= angka2_3005
print("\nAssigment perkalian (*=)")
print("Hasil =",hasil_3005)

# Assigment pembagian, pembagian bulat, dan sisa bagi
if angka2_3005 != 0:
    hasil_3005 = angka1_3005 
    hasil_3005 /= angka2_3005
    print("\nAssigment pembagian (/=)")
    print("Hasil =",hasil_3005)
    # Operator tambahan
    hasil_3005 = angka1_3005 
    hasil_3005 //= angka2_3005
    print("\nAssigment pembagian bulat (//=)")
    print("Hasil =",hasil_3005)
    hasil_3005 = angka1_3005 
    hasil_3005 %= angka2_3005
    print("\nOperator sisa bagi (%=)")
    print("Hasil =",hasil_3005)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assigment perpangkatan
hasil_3005 = angka1_3005 
hasil_3005 **= angka2_3005
print("\nOperator perpangkatan (**=)")
print("Hasil =",hasil_3005)