number_of_rows = 4
seats_per_row = 5
# Write your code below
cinema = []
for i in range(number_of_rows):
    cinema.append(["."] * seats_per_row)

seats_taken = 0

while True:
    for i in range(number_of_rows):
        print(f"Row {i + 1}:", " ".join(cinema[i]))

    row = int(input("Row (0 to stop): "))

    if row == 0:
        break

    seat = int(input("Seat: "))

    if row < 1 or row > number_of_rows or seat < 1 or seat > seats_per_row:
        print("Invalid seat.")
    elif cinema[row - 1][seat - 1] == "X":
        print("Seat already taken.")
    else:
        cinema[row - 1][seat - 1] = "X"
        seats_taken += 1
        print("Seat booked.")

print("Seats taken:", seats_taken)