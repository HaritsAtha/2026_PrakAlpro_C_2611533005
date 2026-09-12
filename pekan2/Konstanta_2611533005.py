# Buat nama dengan nama Konstanta_NIM.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variable ditambah 4 digit nim terakhir contoh: jari_1234

from typing import Final, final
PI: Final = 3.14
print("pi: %f" % PI)
jari_3005 = float(input('Masukkan nilai jari-jari: '))
luas_3005 = PI * jari_3005 * jari_3005
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_3005, luas_3005))