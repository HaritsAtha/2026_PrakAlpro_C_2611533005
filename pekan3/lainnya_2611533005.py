# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas

print("======================================")
print("1. OPERATOR KEANGGOTAAN")
print("======================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_3005 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_3005 = [int(angka.strip()) for angka in input_data_3005.split(",")]

nilai_dicari_3005 = int(input("Masukkan nilai yang ingin dicari: "))

# Operator in
hasil_3005 = nilai_dicari_3005 in data_3005
print("\nOperator keanggotaan IN")
print(nilai_dicari_3005, "in", data_3005, "=", hasil_3005)

# Operator not in
hasil_3005 = nilai_dicari_3005 not in data_3005
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_3005, "not in", data_3005, "=", hasil_3005)


print("======================================")
print("2. OPERATOR IDENTIAS")
print("======================================")

# objek1 menggunakan list dari input perngguna
object1_3005 = data_3005

# objek2 merujuk pada objek yang sama dengan objek1
object2_3005 = object1_3005

# objek3 memiliki isi sama, tetapi merupakan objek baru
object3_3005 = data_3005.copy()

print("object1 =",object1_3005)
print("object2 =",object2_3005)
print("object3 =",object3_3005)

# Operator is
hasil_3005 = object1_3005 is object2_3005
print("\nOperator identitas IS")
print("objek1 is objek2 =",hasil_3005)

# Operator is not
hasil_3005 = object1_3005 is not object3_3005
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =",hasil_3005)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =",object1_3005 is object3_3005)
print("objek1 == objek3 =",object1_3005 == object3_3005)