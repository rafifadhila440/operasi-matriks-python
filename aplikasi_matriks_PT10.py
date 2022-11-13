#Proyek Aplikasi Logika Algoritma 
#Kelompok 

#Penjumlahan
import os
#import numpy as np
def penjumlahan():
    #print("=" * 60)    
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
    mat1 = [
        [(bl1),(bl2),(bl3)],
        [(bl4),(bl5),(bl6)],
        [(bl7),(bl8),(bl9)]
        ]
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
    mat2 = [
        [(bl1),(bl2),(bl3)],
        [(bl4),(bl5),(bl6)],
        [(bl7),(bl8),(bl9)]
        ]
    #mat3 = []
    os.system('cls')

    print("Matriks 1")
    for i in range (3):
        print(mat1[i])
    print("\nMatriks 2")
    for i in range (3): 
        print(mat2[i])

    print("\nHasil Penjumlahan Matriks")
    for x in range(0, len(mat1)):
        jumlah = 0
        row = []
        for y in range(0, len(mat1[0])):
            jumlah = mat1[x][y] + mat2[x][y]
            row.append(jumlah)
        print(row)
    #    mat3.append(row)
    #print(mat3)
    
#Pengurangan
def pengurangan():
    #print("=" * 60)
    print("Pengurangan")
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
    mat1 = [
        [(bl1),(bl2),(bl3)],
        [(bl4),(bl5),(bl6)],
        [(bl7),(bl8),(bl9)]
        ]
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
    mat2 = [
        [(bl1),(bl2),(bl3)],
        [(bl4),(bl5),(bl6)],
        [(bl7),(bl8),(bl9)]
        ]
    #mat3 = []
    os.system('cls')

    print("Matriks 1")
    for i in range (3):
        print(mat1[i])
    print("\nMatriks 2")
    for i in range (3): 
        print(mat2[i])

    print("\nHasil Pengurangan Matriks")
    for x in range(0, len(mat1)):
        jumlah = 0
        row = []
        for y in range(0, len(mat1[0])):
            jumlah = mat1[x][y] - mat2[x][y]
            row.append(jumlah)
        print(row)
    #    mat3.append(row)
    #print(mat3)

#Perkalian
def perkalian():
    #print("=" * 60)
    print("Perkalian")
    print(" ")
    print("Masukan angka untuk Matriks 1")
    print("")
    bl1 =int(input("masukan kolom anda 1: "))
    bl2 =int(input("masukan kolom anda 2: "))
    bl3 =int(input("masukan kolom anda 3: "))
    bl4 =int(input("masukan kolom anda 1: "))
    bl5 =int(input("masukan kolom anda 2: "))
    bl6 =int(input("masukan kolom anda 3: "))
    bl7 =int(input("masukan kolom anda 1: "))
    bl8 =int(input("masukan kolom anda 2: "))
    bl9 =int(input("masukan kolom anda 3: "))
    mat1 = [
        [(bl1),(bl2),(bl3)],
        [(bl4),(bl5),(bl6)],
        [(bl7),(bl8),(bl9)]
        ]
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
    mat2 = [
        [(bl1),(bl2),(bl3)],
        [(bl4),(bl5),(bl6)],
        [(bl7),(bl8),(bl9)]
        ]
    #mat3 = []
    os.system('cls')

    print("Matriks 1")
    for i in range (3):
        print(mat1[i])
    print("\nMatriks 2")
    for i in range (3):
        print(mat2[i])

    print("\nHasil Perkalian Matriks")
    for x in range(0, len(mat1)):
        jumlah = 0
        row = []
        for y in range(0, len(mat1[0])):
            jumlah = mat1[x][y] * mat2[x][y]
            row.append(jumlah)
        print(row)
    #    mat3.append(row)
 #print(mat3)

#Transpose
def transpose():
    #print("=" * 60)
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
    #tanpa menggunakan library numpy
    mat1 = [
        [(bl1),(bl2),(bl3)],
        [(bl4),(bl5),(bl6)],
        [(bl7),(bl8),(bl9)]
        ]
    os.system('cls')

    print("Matriks")
    for i in range (3):
        print(mat1[i])

    result = [[mat1[j][i] for j in range(len(mat1))] for i in range(len(mat1[0]))]
    print("\nHasil Transpose")
    for r in result:
       print(r)

    #menggunakan library numpy
    #mat1 = np.array([[bl1,bl2,bl3],
    #                [bl4,bl5,bl6],
    #                [bl7,bl8,bl9]])
    #os.system('cls')
    #print("Matriks")
    #print(mat1)
    #transpose_matriks = np.transpose(mat1)
    #print("\nTranpose Matriks")
    #print(transpose_matriks)

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