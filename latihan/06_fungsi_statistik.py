# Input: Fungsi rata_rata yang menerima parameter data (list) dan variabel list nilai
def rata_rata(data):
    # Proses: Memeriksa apakah list kosong (kembalikan 0 jika iya) atau menghitung rata-rata elemen
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

nilai = [75, 80, 65, 90, 88]

# Output: Menampilkan hasil kalkulasi rata-rata dari fungsi dengan format 2 desimal
print(f"Rata-rata = {rata_rata(nilai):.2f}")