# Name: Muhammad Farras Agustin
# NIM: 2611533013
# Question 3

text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:11])

text = "Algoritma dan Pemrograman"
count = 0
for char in text:
    if char in "aiueo":
        count += 1
print("Vowels:", count)
