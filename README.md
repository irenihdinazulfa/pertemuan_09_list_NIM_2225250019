# Pertemuan 09 - List dan Pengolahan Data Numerik

Nama: Iren Ihdina Zulfa
NIM: 2225250019
Kelas: Pendidikan Matematika

## Tujuan
Mengolah kumpulan data numerik dengan list Python.

## Struktur Program
- `01_buat_list.py`: Membuat list numerik dan menampilkan isi serta jumlah elemennya.
- `02_indeks_slicing.py`: Mengakses elemen list menggunakan indeks positif/negatif dan teknik slicing.
- `03_manipulasi_list.py`: Melakukan perubahan nilai, penambahan (`append`), penyisipan (`insert`), dan penghapusan (`remove`) pada list.
- `04_agregasi_nilai.py`: Menghitung total (`sum`), rata-rata, nilai minimum (`min`), dan nilai maksimum (`max`).
- `05_filter_kelulusan.py`: Menyaring nilai dalam list berdasarkan batas kelulusan (>= 60).
- `06_fungsi_statistik.py`: Membuat fungsi untuk menghitung rata-rata dari sebuah list.
- `praktik/analisis_nilai_mahasiswa.py`: Program utama untuk melakukan analisis statistik deskriptif dan filter kelulusan mahasiswa menggunakan fungsi.

## Cara Menjalankan
python3 praktik/analisis_nilai_mahasiswa.py

## Test Case
| Data Input | Hasil yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- |
| `[78, 55, 90, 67, 60, 82, 45, 71, 88, 59]` | Total: 695, Rata-rata: 69.50, Min: 45, Max: 90, Lulus: 6, Belum Lulus: 4 | Total: 695, Rata-rata: 69.50, Min: 45, Max: 90, Lulus: 6, Belum Lulus: 4 | PASSED |

## Refleksi
- **Pemahaman:** Indeks pada list Python dimulai dari 0, dan kita bisa menggunakan slicing `[start:stop]` untuk mengambil sub-list secara efisien.
- **Kesalahan yang Diperbaiki:** Sempat terjadi `IndexError` saat mencoba melakukan slicing melebihi rentang indeks, yang berhasil diperbaiki dengan menyesuaikan batas indeks atas pada rentang list.
