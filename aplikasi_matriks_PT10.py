#Proyek Aplikasi Logika Algoritma 
#Kelompok 

#Penjumlahan
import os
def penjumlahan():
    #print("=" * 90)    
    print("Penjumlahan matriks")
    print(" ")
    print("Masukkan angka untuk Matriks 1")
    print(" ")
    bl1 =int(input("masukan kolom anda 1: "))
    bl2 =int(input("masukan kolom anda 2: "))
    bl3 =int(input("masukan kolom anda 3: "))
    bl4 =int(input("masukan kolom anda 1: "))
    bl5 =int(input("masukan kolom anda 2: "))
    bl6 =int(input("masukan kolom anda 3: "))
    bl7 =int(input("masukan kolom anda 1: "))
    bl8 =int(input("masukan kolom anda 2: "))
    bl9 =int(input("masukan kolom anda 3: "))
    matriks1 = ([(bl1),(bl2),(bl3)],[(bl4),(bl5),(bl6)],[(bl7),(bl8),(bl9)])
    os.system('cls')

    print("Masukkan angka untuk Matriks 2")
    print(" ")
    bl1 =int(input("masukan kolom anda 1: "))
    bl2 =int(input("masukan kolom anda 2: "))
    bl3 =int(input("masukan kolom anda 3: "))
    bl4 =int(input("masukan kolom anda 1: "))
    bl5 =int(input("masukan kolom anda 2: "))
    bl6 =int(input("masukan kolom anda 3: "))
    bl7 =int(input("masukan kolom anda 1: "))
    bl8 =int(input("masukan kolom anda 2: "))
    bl9 =int(input("masukan kolom anda 3: "))
    matriks2 = ([(bl1),(bl2),(bl3)],[(bl4),(bl5),(bl6)],[(bl7),(bl8),(bl9)])
    os.system('cls')

    print("Matriks 1")
    for i in range (3):
        print(matriks1[i])

    print("\nMatriks 2")
    for i in range (3): 
        print(matriks2[i])

    #for x in range(0, len(matriks1)):
    #    for y in range(0, len(matriks1[0])):
    #        print (matriks1[x][y] + matriks2[x][y], end=' ')
    #    print

#Pengurangan
def pengurangan():
    #print("=" * 90)
    print("Pengurangan")
    print(" ")

#Perkalian
def perkalian():
    #print("=" * 90)
    print("Perkalian")
    print(" ")

#Transpose
def transpose():
    #print("=" * 90)
    print("Transpose")
    print(" ")

kondisi = True

#Menu pilihan program
while(kondisi == True):
    print('')
    print("Program operasi matriks")
    print("=" * 90)
    print('Menu pilihan')
    print('1. Penjumlahan \t(+)')
    print('2. Pengurangan \t(-)')
    print('3. Perkalian \t(*)')
    print('4. Transpose \t(T)')
    print('5. Keluar (X)')

    pilihan = int(input('Menu yang dipilih -> '))
    os.system('cls')
    if pilihan == 1:
        penjumlahan()
    elif pilihan == 2:
        pengurangan()
    elif pilihan == 3:
        perkalian()
    elif pilihan == 4:
        transpose()
    elif pilihan == 5:
        print("ROGER")
        print("Program diakhiri...")
        print("Sampai Jumpa Lagi :) ")
        kondisi = False
    else:
        print("Maaf input salah")
        print("Opsi tidak tersedia")