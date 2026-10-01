# Buat file dengan nama jumlah_genap_NIM.py
# Buat program untuk Perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input() 

ulang_3013 = int(input("Masukkan nilai batas: "))

jumlah_3013 = 0
for i_3013 in range(1, ulang_3013 + 1):
    if i_3013 % 2 == 0:
        print(i_3013, end="")
        jumlah_3013 = jumlah_3013 + i_3013

        if i_3013 < ulang_3013:
            print(" + ", end="")
        else:
            print(" = ", jumlah_3013, end="")
print()
print("Jumlah =", jumlah_3013)
