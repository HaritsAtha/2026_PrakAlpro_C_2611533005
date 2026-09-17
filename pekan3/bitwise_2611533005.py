# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()

print("======================================")
print("3. OPERATOR BITWISE")
print("======================================")

angka1_3005 = int(input("Masukkan angka bitwise-1: "))
angka2_3005 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =",angka1_3005,"| biner =",bin(angka1_3005))
print("angka1 =",angka2_3005,"| biner =",bin(angka2_3005))

# Bitwise AND
hasil_3005 = angka1_3005 & angka2_3005
print("\nBitwise AND (&)")
print(angka1_3005,"&",angka2_3005,hasil_3005)
print("Biner hasil =",bin(hasil_3005))
print("Biner hasil (8 bit) =",format(hasil_3005,"08b"))

# Bitwise OR
hasil_3005 = angka1_3005 | angka2_3005
print("\nBitwise OR (|)")
print(angka1_3005,"|",angka2_3005,hasil_3005)
print("Biner hasil =",bin(hasil_3005))
print("Biner hasil (8 bit) =",format(hasil_3005,"08b"))

# Bitwise XOR
hasil_3005 = angka1_3005 ^ angka2_3005
print("\nBitwise XOR (^)")
print(angka1_3005,"^",angka2_3005,hasil_3005)
print("Biner hasil =",bin(hasil_3005))
print("Biner hasil (8 bit) =",format(hasil_3005,"08b"))

# Bitwise NOT
hasil_3005 = ~angka1_3005
print("\nBitwise NOT (~)")
print(angka1_3005,"~",angka2_3005,hasil_3005)
print("Biner hasil =",bin(hasil_3005))
print("Biner hasil (8 bit) =",format(hasil_3005,"08b"))

# Bitwise geser kiri
jumlah_geser_3005 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_3005 = angka1_3005 << jumlah_geser_3005
print("\nBitwise geser kiri (<<)")
print(angka1_3005,"<<",jumlah_geser_3005,"=",hasil_3005)
print("Biner hasil =",bin(hasil_3005))
print("Biner hasil (8 bit) =",format(hasil_3005,"08b"))

# Bitwise geser kanan
hasil_3005 = angka1_3005 >> jumlah_geser_3005
print("\nBitwise geser kanan (>>)")
print(angka1_3005,">>",jumlah_geser_3005,"=",hasil_3005)
print("Biner hasil =",bin(hasil_3005))
print("Biner hasil (8 bit) =",format(hasil_3005,"08b"))