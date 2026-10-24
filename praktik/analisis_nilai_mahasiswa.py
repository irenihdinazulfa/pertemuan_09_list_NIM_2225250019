# Input: Fungsi hitung rata-rata
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

# Input: Fungsi filter nilai lulus
def nilai_lulus(data, batas=60):
    lulus = []
    for x in data:
        if x >= batas:
            lulus.append(x)
    return lulus

# Input: Data sekumpulan nilai mahasiswa (10 nilai)
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Proses: Perhitungan statistik dan kelulusan
banyak_data = len(nilai)
total_nilai = sum(nilai)
min_nilai = min(nilai)
max_nilai = max(nilai)
rata_nilai = rata_rata(nilai)

daftar_lulus = nilai_lulus(nilai, batas=60)
jumlah_lulus = len(daftar_lulus)
jumlah_belum_lulus = banyak_data - jumlah_lulus

# Output: Tampilan ringkasan statistik dan kelulusan
print("=" * 45)
print("       RINGKASAN ANALISIS NILAI MAHASISWA     ")
print("=" * 45)
print(f"Data Nilai           : {nilai}")
print(f"Banyak Data          : {banyak_data}")
print("-" * 45)
print(f"Total Nilai          : {total_nilai}")
print(f"Rata-rata Nilai      : {rata_nilai:.2f}")
print(f"Nilai Minimum        : {min_nilai}")
print(f"Nilai Maksimum       : {max_nilai}")
print("-" * 45)
print(f"Batas Kelulusan      : 60")
print(f"Jumlah Lulus         : {jumlah_lulus} mahasiswa")
print(f"Jumlah Belum Lulus   : {jumlah_belum_lulus} mahasiswa")
print(f"Daftar Nilai Lulus   : {daftar_lulus}")
print("=" * 45)