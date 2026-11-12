# Name : Harits Atha Ikhvan
# NIM : 2611533005
# Question 7

name = "Siti Aisyah"
nim = "2610511023"

username = name.strip().split()[0].lower() + nim[-3:]
angkatan = "20" + nim[:2]

print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {angkatan}")
print("=" * 30)