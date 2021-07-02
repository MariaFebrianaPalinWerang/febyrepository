import os
clear = lambda : os.system('cls')

#Perulangan buat Restar Program
jwb = 'y'
while jwb == 'y' or jwb == 'Y' :

    #Daftar List Makanan
    Kode_Menu_Makanan = ['a','b','c','d','e','f']
    Menu_Makanan = ['Nasi Goreng','Lontong Goreng','Bakso Goreng','Rujak Goreng','Rujak Bakso','Rujak Bakso Pecel']
    Harga_Makanan = [15000,14900,12900,13000,15000,17000]

    #Daftar List Minuman
    kode_Menu_Minuman = ['a','b','c','d','e']
    Menu_Minuman = ['Teh dingin hangat','Kopi Dingin','Kopi Teh Panas','coca cola dingin','cocacola panas']
    Harga_Minuman = [2500,5000,6500,3500,500]

    #Tampilan Interfaces

    clear()
    print("=====================================")
    print(" Kantin Fakultas Teknologi Informasi ")
    print("=====================================")

    #Keterangan Pilihan Operasi
    print("Pilihan Operasi")
    print(">> 1. Beli Makanan ")
    print(">> 2. Beli Minuman ")

    #Inputtan Pilihan Operasi
    print("=====================================")
    pilihanoperasi = int(input("Masukkan Pilihan Operasi = "))

    #Cek Pilihan Operasi masuk kriteria mana
    if pilihanoperasi == 1 :
        #Tampilkan List Menu Makanan
        print("=====================================")
        print("           MENU MAKANAN")
        print("=====================================")
        i = 0 
        while i < len(Kode_Menu_Makanan):
            print('---------------------------------')
            print('Kode Menu Makanan : ' + Kode_Menu_Makanan[i])
            print('Menu Makanan      : ' + Menu_Makanan[i])
            print('Harga Makanan     : Rp.' + str(format(Harga_Makanan[i],',.2f')))
            i = i + 1
                    
        #inputan pilihan makanan dan qty makanan
        print("=====================================")
        belimakanan = input("Masukkan Pilihan Makanan : ")
        qtymakanan = int(input("Masukkan qty Makanan = "))
            
        #perulangan cek idx kode menu makanan apakah sama dengan inputan
        i = 0
        while i < len(Kode_Menu_Makanan):
            if Kode_Menu_Makanan[i] == belimakanan :
                #Hitung bayar  
                tothrgmakan = Harga_Makanan[i] * qtymakanan
                #Tampilkan rincian Pembelian
                clear()
                print("=====================================")
                print(">>> RINCIAN PEMBELIAN") 
                print("> Qty Makanan       : " + str(qtymakanan)+" Porsi")
                print("> Menu Makanan      : " + Menu_Makanan[i])
                print('> Harga Makanan     : Rp.' + str(format(Harga_Makanan[i],',.2f')))
                print('> Total Harga       : Rp.' + format(tothrgmakan,',.2f'))
                
                #buat inputtan buat bayar
                print("=====================================")
                bayar = int(input("Masukkan Jumlah Bayar = "))
                
                #set Nilai kembalian
                kembalian = bayar - tothrgmakan
                
                #Tampilkan Hasil
                print("=====================================")
                print(">>> NOTA TRANSAKSI")
                print("> Jumlah Bayar = Rp." + format(bayar,',.2f'))
                print("> Kembalian    = Rp." + format(kembalian,',.2f'))
            i = i + 1
        
    elif pilihanoperasi == 2 :
        #Tampilkan List Menu Minuman 
        i = 0
        while i < len(kode_Menu_Minuman):
            print('---------------------------------')
            print('Kode Menu Minuman : ' + kode_Menu_Minuman[i])
            print('Menu Minuman      : ' + Menu_Minuman[i])
            print('Harga Minuman     : Rp.' + str(format(Harga_Minuman[i],',.2f')))
            i = i + 1
            
        #inputan pilihan makanan dan qty makanan
        print("=====================================")
        beliminuman = input("Masukkan Pilihan Minuman : ")
        qtyminuman = int(input("Masukkan qty Minuman = "))
        
        #perulangan cek idx kode menu makanan apakah sama dengan inputan
        i = 0
        while i < len(Menu_Minuman) :
            if kode_Menu_Minuman[i] == beliminuman :
                #Hitung bayar  
                tothrgminum = Harga_Minuman[i] * qtyminuman
                #Tampilkan rincian Pembelian
                clear()
                print("=====================================")
                print(">>> RINCIAN PEMBELIAN") 
                print("> Qty Minuman       : " + str(qtyminuman)+" Gelas")
                print("> Menu Minuman      : " + Menu_Minuman[i])
                print('> Harga Minuman     : Rp.' + str(format(Harga_Minuman[i],',.2f')))
                print('> Total Harga       : Rp.' + format(tothrgminum,',.2f'))
                
                #buat inputtan buat bayar
                print("=====================================")
                bayarMinum = int(input("Masukkan Jumlah Bayar = "))
                
                #set Nilai kembalian
                KembalianM = bayarMinum - tothrgminum
                
                #Tampilkan Hasil
                print("=====================================")
                print(">>> NOTA TRANSAKSI")
                print("> Jumlah Bayar = Rp." + format(bayarMinum,',.2f'))
                print("> Kembalian    = Rp." + format(KembalianM,',.2f'))
                
            i = i + 1 
                        
    else :
        print("Periksa Kembali Inputan Anda")
    #Inputan untuk mengulangi program
    print("=====================================")
    jwb = input("Ulangi Program? (y/t) : ")
    if jwb == "t" or jwb == "T":
            break








    