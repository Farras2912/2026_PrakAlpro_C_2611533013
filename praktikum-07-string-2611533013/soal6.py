# Name: Muhammad Farras Agustin
# NIM: 2611533013
# Question 6

full_name = " Muhammad Farras Agustin "
nim = "2611533013"

# Menghilangkan spasi di awal dan akhir
clean = full_name.strip()

# Mencari posisi spasi pertama
space = clean.find(" ")

# Mengambil nama depan
if space == -1:
    first_name = clean
else:
    first_name = clean[:space]

# Membuat username
username = first_name.lower() + nim[-3:]

print(username)