# Input: List angka nilai
nilai = [75, 80, 65, 90, 88]

# Proses: Menghitung total (sum), rata-rata (sum/len), nilai terkecil (min), dan nilai terbesar (max)

# Output: Menampilkan hasil perhitungan statistik deskriptif dasar ke layar
print(f"Total = {sum(nilai)}")
print(f"Rata-rata = {sum(nilai)/len(nilai):.2f}")
print(f"Minimum = {min(nilai)}")
print(f"Maksimum = {max(nilai)}")