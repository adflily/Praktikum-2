# Data
barang = ["Buku", "Pensil", "Pulpen"]
harga = [20000, 3000, 5000]
jumlah = [2, 5, 3]

# 1
Harga_Buku = harga[0] * jumlah[0]
print(f' Buku : {Harga_Buku}')
       
Harga_Pensil = harga[1] * jumlah[1]
print(f' Pensil : {Harga_Pensil}')

Harga_Pulpen = harga[2] * jumlah[2]
print(f' Pulpen : {Harga_Pulpen}')

# 2
total_harga_barang = [Harga_Buku, Harga_Pensil, Harga_Pulpen]
print(total_harga_barang)

# 3
total_belanja = total_harga_barang[0] + total_harga_barang[1] + total_harga_barang[2]
print({total_belanja})

# 4
result = {"Buku" : 40000, "Pensil" : 15000, "Pulpen" : 15000, "Total Belanja" : 70000}
print(result)

# 5
print(Harga_Buku > Harga_Pulpen)
print(total_belanja > 50000)

jumlah_barang = jumlah[0] + jumlah[1] + jumlah[2]
print(jumlah_barang > 5)
