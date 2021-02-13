# Christina Andrea Putri - Universitas Kristen Duta Wacana

#Pak Budi membeli sebuah mobil seharga Rp100.000.000,00 secara mencicil. Sebagai pembayaran awal dia 
# membayar sebesar Rp20.000.000,00. Setiap bulannya ia mencicil sebesar Rp 500.000,00. 
# Berapa estimasi bulan dan tahun hutangnya akan lunas?

#Input : harga mobil, pembayaran awal, cicilan per bulan

#Proses : sisa pembayaran yang harus dilakukan, lama bulan mencicil, lama tahun mencicil

#Output : estimasi bulan dan tahun hutang akan lunas 

harga_beli = int(input("Harga beli mobil: Rp "))
byr_awal = int(input("Pembayaran awal : Rp "))
cicilan = int(input("Cicilan per bulan: Rp "))

sisa_byr = harga_beli-byr_awal
lama_bulan = sisa_byr/cicilan
lama_thn = lama_bulan/12 

print("Estimasi bulan hutang akan lunas : ", int(lama_bulan), "bulan")
print("Estimasi tahun hutang akan lunas : ", int(lama_thn), "tahun" )