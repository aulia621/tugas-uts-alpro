def inputan(listrik):
    wat = int(input(f"Masukkan wat {listrik} = "))
    durasi = int(input(f"Masukkan waktu pemakaian {listrik} = "))
    return wat, durasi

def hitung_kwh(wat, durasi):
    hitung_wat = wat * durasi
    hitung_kwh = hitung_wat / 1000
    return hitung_kwh

def hitung_harga(kwh):
     total_harga = kwh * 1500
     return total_harga

# Program utama
daya_a, waktu_a = inputan("kipas")
daya_b, waktu_b = inputan("TV")
daya_c, waktu_c = inputan("lampu")

proses_kwh_1 = hitung_kwh(daya_a, waktu_a)
proses_kwh_2 = hitung_kwh(daya_b, waktu_b)
proses_kwh_3 = hitung_kwh(daya_c, waktu_c )
total_kwh = proses_kwh_1 + proses_kwh_2 +proses_kwh_3

harga_1 = hitung_harga(proses_kwh_1)
harga_2 = hitung_harga(proses_kwh_2)
harga_3 = hitung_harga(proses_kwh_3)

print()

print(f"kwh yang dihasilkan kipas per hari : {proses_kwh_1:,.2f}")
print(f"kwh yang dihasilkan TV per hari : {proses_kwh_2:,.2f}")
print(f"kwh yang dihasilkan lampu per hari : {proses_kwh_3:,.2f}")
print(f"total kwh yang dihasilkan semua alat : {total_kwh:,.2f}")

print()

print(f"Biaya penggunaan kipas: Rp {harga_1:,.0f}")
print(f"Biaya penggunaan TV: Rp {harga_2:,.0f}")
print(f"Biaya penggunaan lampu: Rp {harga_3:,.0f}")

print()

total_kwh_hari = proses_kwh_1 + proses_kwh_2 + proses_kwh_3
total_bulan = total_kwh_hari * 30

print(f"total dalam satu hari adalah: {total_kwh_hari:,.3f} ")
print(f"total dalam satu bulan adalah:  {total_bulan:,.3f}" )
