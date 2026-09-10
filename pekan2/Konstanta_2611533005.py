from typing import Final, final
PI: Final = 3.14
print("pi: %f" % PI)
jari_3005 = float(input('Masukkan nilai jari-jari: '))
luas_3005 = PI * jari_3005 * jari_3005
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_3005, luas_3005))