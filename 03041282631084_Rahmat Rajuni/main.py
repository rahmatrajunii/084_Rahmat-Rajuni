analisis_dan_klasifikasi_data = [42, 55, 61, 68, 73,
                                79, 82, 87, 91, 64,
                                58, 76, 84, 49, 95,
                                10, 79, 81, 80, 99] #data tambahan

# hitung kategori nilai (clear)
# hitung rata-rata data (clear)
# hitung kategori data (clear)

def rata_rata(data):
    total = 0
    for nilai in data:
        total += nilai
    return total / len(data)

def hitung_kategori(nilai):
    if nilai < 60:
        return "rendah"
    elif 60 <= nilai < 80:
        return "sedang"
    else:
        return "tinggi"

print("Rata-rata data:", rata_rata(analisis_dan_klasifikasi_data) )

print("hitung kategori")
for nilai in analisis_dan_klasifikasi_data:
    print(nilai, "=", hitung_kategori(nilai))

def jumlah_kategori (data):
    rendah = 0
    sedang = 0
    tinggi = 0
    for nilai in data:
        status = hitung_kategori(nilai)
        if status == "rendah":
            rendah += 1
        elif status == "sedang":
            sedang += 1
        else:
            tinggi += 1
    return rendah, sedang, tinggi
rendah, sedang, tinggi = jumlah_kategori(analisis_dan_klasifikasi_data)
print("jumlah kategori:")
print("RENDAH:", rendah)
print("SEDANG:", sedang)
print("TINGGI:", tinggi)

print ("=== MENGANALISIS DAN MENGKLASIFIKASI DATA ===")

for i in range(len(analisis_dan_klasifikasi_data)):
    kategori = analisis_dan_klasifikasi_data[i]
    status = hitung_kategori(kategori)
    print("Data ke", i+1, "->", kategori, "=", status)

rendah, sedang, tinggi = jumlah_kategori(analisis_dan_klasifikasi_data)
average = rata_rata(analisis_dan_klasifikasi_data)

print()
print("=== RINGKASAN ===")
print("total kategori:", len(analisis_dan_klasifikasi_data))
print("RENDAH:", rendah)
print("SEDANG:", sedang)
print("TINGGI:", tinggi)
print("rata-rata nlai:", round(average, 2))
print("nilai terkecil:", min(analisis_dan_klasifikasi_data))
print("nilai terbesar:", max(analisis_dan_klasifikasi_data))