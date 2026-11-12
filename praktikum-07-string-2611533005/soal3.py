# Name : Harits Atha Ikhvan
# NIM : 2611533005
# Question 3

#-----Bagian A-----
text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

#-----Bagian B-----
text = "Harits Atha Ikhvan"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)
