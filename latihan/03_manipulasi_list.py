# Input: List awal nilai dengan 3 elemen
nilai = [75, 80, 65]

# Proses: 
# 1. Mengubah nilai elemen pada indeks 1 menjadi 82
# 2. Menambahkan nilai 90 di akhir list (append)
# 3. Menyisipkan nilai 70 pada indeks 1 (insert)
# 4. Menghapus elemen bermuatan angka 65 (remove)
nilai[1] = 82
nilai.append(90)
nilai.insert(1, 70)
nilai.remove(65)

# Output: Menampilkan isi list setelah seluruh operasi manipulasi dilakukan
print(nilai)