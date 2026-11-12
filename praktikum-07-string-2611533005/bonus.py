# Name : Harits Atha Ikhvan
# NIM : 2611533005
# bonus

kalimat = input("Masukkan kalimat: ")
teks = kalimat.replace(" ", "").lower()

if teks == teks[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")