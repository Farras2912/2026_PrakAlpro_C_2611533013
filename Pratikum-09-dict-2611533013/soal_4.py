absen = {"1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10" , "11" , "12" , "13" , "14"}
tugas = {}
count = {}

for submitted in tugas :
    if tugas in count :
        count[tugas] = count[tugas] + 1
    else:
        count[tugas] = 1
print(count)