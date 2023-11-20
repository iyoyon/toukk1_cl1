import os

#asc
def urutasc(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                simpan=a[j]
                a[j]=a[j+1]
                a[j+1]=simpan
    print(a)

#desc
def urutdesc(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]<a[j+1]:
                simpan=a[j]
                a[j]=a[j+1]
                a[j+1]=simpan
    print(a)

#pengulangan
while(True):
    os.system('cls')
    #Tampil judul
    print("===========================")
    print("Program Mengurutkan Data")
    print("Dengan Metode Bubble Short")
    print("===========================")

    #input 10 bilangan
    bil1=int(input("Masukkan bilangan ke-1 : "))
    bil2=int(input("Masukkan bilangan ke-2 : "))
    bil3=int(input("Masukkan bilangan ke-3 : "))
    bil4=int(input("Masukkan bilangan ke-4 : "))
    bil5=int(input("Masukkan bilangan ke-5 : "))
    bil6=int(input("Masukkan bilangan ke-6 : "))
    bil7=int(input("Masukkan bilangan ke-7 : "))
    bil8=int(input("Masukkan bilangan ke-8 : "))
    bil9=int(input("Masukkan bilangan ke-9 : "))
    bil10=int(input("Masukkan bilangan ke-10 : "))

    #tampil pilihan urut
    print("=========================")
    print("Pilihan metode pengurutan :")
    print("1.Sorting Ascending")
    print("2.Sorting Descending")

    #merubah input bilangan menjadi list
    bil=[bil1,bil2,bil3,bil4,bil5,bil6,bil7,bil8,bil9,bil10]
    
    #tampil hasil
    pilih=input("Metode yang dipilih : ")
    print("=========================")

    print("Data sebelum diurutkan : ")
    print(bil)
    print('Nilai Maksimal : ',max(bil))
    print('Nilai Minimal : ',min(bil))
    print('Nilai Rerata : ',sum(bil)/len(bil))
    print("Data sesudah diurutkan : ")

#Pemilihan urutan dengan pencabangan    
    if pilih=="1":
        urutasc(bil)
    elif pilih=="2":
        urutdesc(bil)
    else:
        print("Pilihan tidak ada")

    #input pengulangan
    menu=input("Kembali ke menu awal (Y/N)?")

    #pilihan pengulangan, Ya atau No
    if menu=="N" or menu=="n":
        print("Selesai, Terimakasih!")
        break
    elif menu!="Y" and menu!="y":
        print("Pilihan tidak ada!")
        break
