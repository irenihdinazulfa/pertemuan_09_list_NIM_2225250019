# Input: List angka nilai dan list kosong untuk menampung nilai lulus
nilai = [75, 55, 80, 60, 45, 90]
lulus = []

# Proses: Melakukan perulangan untuk memeriksa setiap elemen, lalu menyaring nilai yang >= 60 ke dalam list lulus

# Output: Menampilkan daftar nilai yang lulus beserta total jumlah datanya
for x in nilai:
    if x >= 60:
        lulus.append(x)

print(f"Nilai lulus = {lulus}")
print(f"Jumlah lulus = {len(lulus)}")