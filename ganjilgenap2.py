# Program Pengecekan Angka Ganjil / Genap dengan Perulangan

print("=== PROGRAM PENGECEKAN GANJIL / GENAP ===")
print("Ketik 'x' atau 'n' kapan saja untuk menutup program.\n")

while True:
    # Meminta masukan dari pengguna
    input_user = input("Masukkan sebuah angka: ").strip().lower()

    # Kondisi untuk menghentikan program (tombol/karakter close)
    if input_user == 'x' or input_user == 'n':
        print("\nProgram selesai. Terima kasih!")
        break

    # Pengecekan apakah input berupa angka valid
    try:
        angka = int(input_user)
        
        # Logika if-else untuk penentuan ganjil/genap
        if angka % 2 == 0:
            print(f"-> Angka {angka} adalah GENAP.\n")
        else:
            print(f"-> Angka {angka} adalah GANJIL.\n")
            
    except ValueError:
        print("-> Input tidak valid! Silakan masukkan angka bulat atau 'x' untuk keluar.\n")