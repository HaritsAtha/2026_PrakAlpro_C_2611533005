# Buat file dengan nama nested_for4_NIM.py
# Buat program untuk perulangna dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_3005 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_3005 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_3005 = tinggi_3005
    c_3005 = a_3005
    lebar_3005 = (2*tinggi_3005) - 2

    for i_3005 in range(1, tinggi_3005 + 1):
        b_3005 = c_3005 + 1

        for j_3005 in range(1, lebar_3005 + 1):

            # Baris atas dan bawah
            if i_3005 == 1 or i_3005 == tinggi_3005:
                if j_3005 == 1 or j_3005 == lebar_3005:
                    print("#", end="")
                else:
                    print("=", end="")

            # Baris isi
            else:
                if j_3005 == 1 or j_3005 == lebar_3005:
                    print("|", end="")
                else:
                    if j_3005 == c_3005:
                        print("<", end="")
                    elif j_3005 == b_3005:
                        print(">", end="")
                    elif j_3005 == (lebar_3005 - c_3005):
                        print("<", end="")
                    elif j_3005 == (lebar_3005 - c_3005 + 1):
                        print(">", end="")
                    elif j_3005 > b_3005 and j_3005 < (lebar_3005 - c_3005):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # Logika asli Java
        a_3005 -= 2

        if a_3005 <= 0:
            c_3005 = (-a_3005) + 2
        else:
            c_3005 = a_3005