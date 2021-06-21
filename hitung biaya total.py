kode =['A','B']


kota = ['Surabaya','Bandung']
jarak = [169,452]
ongkirperkm = [2500,4000]


print ("=============================================")
print(" TRANSAKSI BIAYA EKSPEDISI ")
print ("=============================================")
print(" Kode = A. ",kota[0])
print(" Kode = B. ",kota[1])
print ("=============================================")

pilihan = input(">> Masukkan Kode Tujuan = ")

if pilihan=="a":
    idx = 0
elif pilihan=="b":
    idx = 1
else:
    idx = 0


print("Pilihan Tujuan = " + kota[idx])
print("Jarak          = " + str(jarak[idx]) + " km")
print("Ongkir per km  = Rp. " + str(ongkirperkm[idx]))


fixjarak = jarak[idx]
fixongkirkm = ongkirperkm[idx]
totongkir = fixjarak * fixongkirkm

print("-------------------------------------")
print("Total Biaya     = Rp." + str(totongkir))