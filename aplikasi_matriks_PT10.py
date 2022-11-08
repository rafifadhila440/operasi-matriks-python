#Proyek Aplikasi Logika Algoritma 
#Kelompok 

#Penjumlahan
import os
def penjumlahan():
    #print("=" * 90)    
    print("penjumlahan")
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
    matriks = ([(bl1),(bl2),(bl3)],[(bl4),(bl5),(bl6)],[(bl7),(bl8),(bl9)])

    for i in range (3): 
        print(matriks[i])

#Pengurangan
def pengurangan():
    #print("=" * 90)
    print("Pengurangan")
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
    matriks = ([(bl1),(bl2),(bl3)],[(bl4),(bl5),(bl6)],[(bl7),(bl8),(bl9)])

    for i in range (3): 
        print(matriks[i])

#Perkalian
def perkalian():
    #print("=" * 90)
    print("Perkalian")
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
    matriks = ([(bl1),(bl2),(bl3)],[(bl4),(bl5),(bl6)],[(bl7),(bl8),(bl9)])

    for i in range (3): 
        print(matriks[i])

#Transpose
def transpose():
    #print("=" * 90)
    print("Transpose")
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
    matriks = ([(bl1),(bl2),(bl3)],[(bl4),(bl5),(bl6)],[(bl7),(bl8),(bl9)])

    for i in range (3): 
        print(matriks[i])

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