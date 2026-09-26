# Buat file dengan nama if_elif_else1_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input() 

umur_3013 = int(input("Input umur Anda: "))
sim_3013 = input("Apakah Anda Sudah Punya Sim C (y/t): ") [0]

if umur_3013 >= 17 and sim_3013 == 'y':
    print("Anda Sudah dewasa dan boleh bawa motor")
elif umur_3013 >= 17 and sim_3013 != 'y':
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")
elif umur_3013 < 17 and sim_3013 == 'y':
    print("Anda Belum Cukup Umur punya SIM")
else:
    print("Anda Belum Cukup Umur dan tidak boleh bawa motor")
print("Program Selesai")