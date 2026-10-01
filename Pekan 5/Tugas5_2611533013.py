batas_3013 = int(input("Masukkan nilai segi tiga: "))
for i_3013 in range(1, batas_3013 + 1):
    for j_3013 in range(batas_3013 - i_3013):
        print(" ", end="")
    for k_3013 in range(i_3013):
        print("*", end=" ")
    print()  