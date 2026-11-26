schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

busiest_day = ""
highest = 0

for day in schedule:
    if len(schedule[day]) > highest:
        highest = len(schedule[day])
        busiest_day = day

print(f"Busiest day: {busiest_day} ({highest} courses)")

course = input("Enter course name: ")
count = 0

for day in schedule:
    if course in schedule[day]:
        count += 1

print(f"{course}: {count} days")