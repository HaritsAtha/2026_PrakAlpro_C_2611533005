list_absen = input().split()
list_kumpul = input().split()

absen_set = set(list_absen)
kumpul_set = set(list_kumpul)

kumpul = absen_set & kumpul_set
tidak_kumpul = absen_set - kumpul

print("Submitted: ", len(kumpul), "students")
print("Not submitted: ", len(tidak_kumpul), "students")

for number in list_absen:
    if number not in kumpul:
        print(number)