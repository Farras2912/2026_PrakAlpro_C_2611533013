# Name: Muhammad Farras Agustin
# NIM: 2611533013
# Question 5

username = input("Username: ")
username = input("Username: ")

if len(username) < 5:
    print("Invalid: at least 5 characters")
elif not username.isalnum():
    print("Invalid: letters and digits only")
elif not username[0].isalpha():
    print("Invalid: must start with a letter")
else:
    print("Valid")

nim = input("Masukkan NIM: ")

if len(nim) == 10 and nim.isdigit():
    tahun = nim[:2]
    print("Valid, intake year 20" + tahun)
else:
    print("Invalid NIM")