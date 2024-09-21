Cara Menjalankan Program Cipher
Program cipher ini bertujuan untuk mengenkripsi dan mendekripsi pesan menggunakan algoritma cipher yang telah diimplementasikan. Berikut adalah langkah-langkah untuk menjalankan program:

Persyaratan Sistem
Pastikan Anda telah menginstal beberapa hal berikut:

Python 3.x: Program ini ditulis menggunakan Python, jadi pastikan Python telah terpasang di sistem Anda. Anda bisa mengunduhnya di python.org.
Library Tambahan (jika ada): Jika program menggunakan library eksternal, pastikan untuk menginstalnya terlebih dahulu dengan menjalankan perintah:
Copy code
pip install -r requirements.txt
Langkah-langkah Menjalankan Program
Clone atau Download Repositori
Unduh atau clone repositori ini ke direktori lokal Anda:

bash
Copy code
git clone <URL_REPOSITORI>
Masuk ke Direktori Program
Pindah ke folder program yang telah di-clone atau di-download:

bash
Copy code
cd <nama_folder_program>
Jalankan Program Cipher
Untuk menjalankan program, gunakan perintah berikut di terminal atau command prompt:

Copy code
python cipher.py
Masukkan Input
Setelah menjalankan program, Anda akan diminta untuk memasukkan pilihan operasi:

Pilih 1 untuk enkripsi pesan.
Pilih 2 untuk dekripsi pesan.
Kemudian, masukkan pesan dan kunci yang ingin digunakan sesuai instruksi yang diberikan oleh program.

Output
Setelah proses enkripsi atau dekripsi selesai, hasilnya akan ditampilkan di terminal.

Contoh Penggunaan
Contoh input dan output dalam program:

Enkripsi:

yaml
Copy code
Pilih operasi (1 untuk Enkripsi, 2 untuk Dekripsi): 1
Masukkan pesan: hello
Masukkan kunci: 3
Pesan terenkripsi: khoor
Dekripsi:

yaml
Copy code
Pilih operasi (1 untuk Enkripsi, 2 untuk Dekripsi): 2
Masukkan pesan: khoor
Masukkan kunci: 3
Pesan terdekripsi: hello
Catatan
Program ini hanya mendukung alfabet huruf kecil. Pastikan pesan dan kunci sesuai dengan batasan yang diberikan.