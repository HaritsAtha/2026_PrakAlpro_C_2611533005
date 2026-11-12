# Name : Harits Atha Ikhvan
# NIM : 2611533005
# Question 6

#-----Pemanasan-----
first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())
#--------------------

full_name = "Harits Atha Ikhvan"
nim = "2611533005"
 
# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().

clean_name = full_name.strip()
space_index = clean_name.find(" ")

if space_index == -1:
    first_name = clean_name
else:
    first_name = clean_name[:space_index]

username = first_name.lower() + nim[-3:]

print(username)