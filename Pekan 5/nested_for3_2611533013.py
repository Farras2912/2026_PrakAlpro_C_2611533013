# Buat file dengan nama nested_for3_NIM.py
# Buat program untuk Perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input() 

batas_3013 = int(input("Masukkan nilai batas: "))
for i_3013 in range(batas_3013+1):
    for j_3013 in range(batas_3013+1):
        print(i_3013+j_3013, end=" ")
    print()   # pindah ke baris berikutnya  