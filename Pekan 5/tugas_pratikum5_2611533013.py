print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

n_3013 = int(input("Masukkan ukuran skala jam pasir (N): "))

# Membuat garis atas
print("#", end="")

for j_3013 in range(4 * n_3013 + 5):
    print("=", end="")

print("#")

# Fase 1: Jam pasir atas (baris N turun sampai 1)
for baris_3013 in range(n_3013, 0, -1):

    # Garis tegak kiri dan satu spasi padding
    print("| ", end="")

    # Spasi penyeimbang kiri
    for spasi_3013 in range(2 * (n_3013 - baris_3013)):
        print(" ", end="")

    # Angka menurun
    for angka_3013 in range(baris_3013, 0, -1):
        print(angka_3013, end=" ")

    # Poros kristal tengah
    print("<*>", end="")

    # Angka menaik (diawali spasi)
    for angka_3013 in range(1, baris_3013 + 1):
        print(" " + str(angka_3013), end="")

    # Spasi penyeimbang kanan
    for spasi_3013 in range(2 * (n_3013 - baris_3013)):
        print(" ", end="")

    # Satu spasi padding dan garis tegak kanan
    print(" |")

# Fase 2: Poros titik pusat
print("|", end="")

for spasi_3013 in range(2 * n_3013 + 1):
    print(" ", end="")

print("<*>", end="")

for spasi_3013 in range(2 * n_3013 + 1):
    print(" ", end="")

print("|")

# Fase 3: Jam pasir bawah (baris 1 naik sampai N)
for baris_3013 in range(1, n_3013 + 1):

    # Garis tegak kiri dan satu spasi padding
    print("| ", end="")

    # Spasi penyeimbang kiri
    for spasi_3013 in range(2 * (n_3013 - baris_3013)):
        print(" ", end="")

    # Angka menurun
    for angka_3013 in range(baris_3013, 0, -1):
        print(angka_3013, end=" ")

    # Poros kristal tengah
    print("<*>", end="")

    # Angka menaik (diawali spasi)
    for angka_3013 in range(1, baris_3013 + 1):
        print(" " + str(angka_3013), end="")

    # Spasi penyeimbang kanan
    for spasi_3013 in range(2 * (n_3013 - baris_3013)):
        print(" ", end="")

    # Satu spasi padding dan garis tegak kanan
    print(" |")

# Membuat garis bawah
print("#", end="")

for j_3013 in range(4 * n_3013 + 5):
    print("=", end="")

print("#")