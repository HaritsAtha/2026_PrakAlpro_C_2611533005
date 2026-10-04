n_3005 = int(input("Masukkan ukuran skala jam pasir (N): "))

lebar_3005 = 4 * n_3005 + 7

for j_3005 in range(lebar_3005):
    if j_3005 == 0 or j_3005 == lebar_3005 - 1:
        print("#", end="")
    else:
        print("=", end="")
print()

for baris_3005 in range(n_3005, 0, -1):
    print("|", end="")

    spasi_3005 = 2 * (n_3005 - baris_3005) + 1
    for j_3005 in range(spasi_3005):
        print(" ", end="")

    for angka_3005 in range(baris_3005, 0, -1):
        print(angka_3005, end=" ")

    print("<*>", end="")

    for angka_3005 in range(1, baris_3005 + 1):
        print(" ", end="")
        print(angka_3005, end="")

    for j_3005 in range(spasi_3005):
        print(" ", end="")

    print("|")

print("|", end="")

spasi_3005 = 2 * n_3005 + 1
for j_3005 in range(spasi_3005):
    print(" ", end="")

print("<*>", end="")

for j_3005 in range(spasi_3005):
    print(" ", end="")

print("|")

for baris_3005 in range(1, n_3005 + 1):
    print("|", end="")

    spasi_3005 = 2 * (n_3005 - baris_3005) + 1
    for j_3005 in range(spasi_3005):
        print(" ", end="")

    for angka_3005 in range(baris_3005, 0, -1):
        print(angka_3005, end=" ")

    print("<*>", end="")

    for angka_3005 in range(1, baris_3005 + 1):
        print(" ", end="")
        print(angka_3005, end="")

    for j_3005 in range(spasi_3005):
        print(" ", end="")

    print("|")

for j_3005 in range(lebar_3005):
    if j_3005 == 0 or j_3005 == lebar_3005 - 1:
        print("#", end="")
    else:
        print("=", end="")
print()