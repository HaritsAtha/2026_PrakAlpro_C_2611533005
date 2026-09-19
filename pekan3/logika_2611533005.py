# Buat file dengan nama logika_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# program ini menggunakan fungsi input()
# Program operator logika dalam Python

# Memasukkan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_3005 = input("Input nilai boolean-1 (True/False): ").strip().lower() == "true"
a2_3005 = input("Input nilai boolean-2 (True/False): ").strip().lower() == "true"

print("\nA1 = ", a1_3005)
print("A2 = ", a2_3005)

# Konjungsi: bernilai True jika keduanya True
hasil_3005 = a1_3005 and a2_3005
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_3005)

# Disjungsi: bernilai True jika salah satunya True
hasil_3005 = a1_3005 or a2_3005
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil_3005)

# Negasi A1: membalik nilai A1
hasil_3005 = not a1_3005
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_3005)

# Negasi A2: membalik nilai A2
hasil_3005 = not a2_3005
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_3005)

# XOR: bernilai True jika kedua nilai berbeda  
hasil_3005 = a1_3005 != a2_3005
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil_3005)