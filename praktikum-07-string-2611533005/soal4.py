# Name : Harits Atha Ikhvan
# NIM : 2611533005
# Question 4

phone = "082611533005"
masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]
print(masked)