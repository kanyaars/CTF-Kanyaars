# Challenge Progress: Blessed (Crypto)

```
cd "/mnt/c/Users/User/OneDrive/Documents/catatan gue/CTF-Kanyaars/CTF Try Out/Crypto/Blessed/crypto_blessed"
python3 -m venv bls_env
source bls_env/bin/activate
pip install py_ecc
pip install pwntools
pip install pycryptodome
python3 exploit.py
```

### **1. Pembuatan Robot yang Terverifikasi (Verified Robots):**

* **Proses Pembuatan Robot:**

  * Kita berhasil membuat robot-robot yang terverifikasi menggunakan perintah `create`.
  * Robot yang dibuat berhasil diverifikasi secara lokal dengan `sk` yang valid dan menghasilkan public key (`pk`).
* **Robot yang Dibuat:**

  * Setiap robot yang dibuat memiliki ID unik (`robot_id`), yang dapat digunakan untuk berinteraksi lebih lanjut dengan server.
  * ID robot ini digunakan untuk mengumpulkan tanda tangan dan juga untuk membedakan robot-robot buatan server dengan robot buatan kita.

### **2. Penandatanganan dan Penggabungan Tanda Tangan (Signatures):**

* **Pembuatan Tanda Tangan:**

  * Tanda tangan (`sig`) untuk pesan yang relevan (`unveil_secrets`) dibuat menggunakan `sk` masing-masing robot yang kita buat.
* **Penggabungan Tanda Tangan:**

  * Semua tanda tangan tersebut digabungkan menjadi satu tanda tangan agregat (`agg_sig`) yang dapat digunakan untuk validasi lebih lanjut di server.
* **Verifikasi Tanda Tangan:**

  * Verifikasi lokal dari tanda tangan agregat berhasil, yang menunjukkan bahwa proses pembuatan dan penggabungan tanda tangan berjalan dengan benar.

### **3. Penelusuran Robot-robot Buatan Server (Server-Made Robots):**

* **Daftar Robot dari Server:**

  * Server memberikan daftar robot-robot yang sudah dibuatnya.
  * Beberapa robot dalam daftar tersebut merupakan robot-robot yang sudah terverifikasi atau gagal diverifikasi (terdeteksi dengan `robot_id` dan `pk` mereka).
* **Penandaan Robot Buatan Server:**

  * Robot-robot yang bukan buatan kita dapat dikenali berdasarkan perbandingan `robot_id`.
  * Server-made robots ini dicatat dan diproses lebih lanjut untuk mencoba mengekstraksi `sk` mereka.

### **4. Coba Mengambil `sk` dari Robot Buatan Server:**

* **Verifikasi dan Eksploitasi:**

  * Script mencoba untuk mengakses dan mengidentifikasi apakah server telah membocorkan `sk` untuk robot buatan server.
  * Beberapa server-made robots gagal diverifikasi atau tidak ada `sk` yang terleak.
  * Dalam beberapa kasus, terjadi kesalahan atau exception saat mencoba memverifikasi robot-robot tersebut dan memperoleh `sk` mereka.
* **Masalah yang Dihadapi:**

  * Tidak semua robot buatan server mengungkapkan `sk` mereka. Ada kemungkinan bahwa server menggunakan mekanisme proteksi yang lebih ketat pada robot-robot tersebut.
  * Error terjadi saat mencoba memverifikasi `sk` atau melakukan percakapan dengan server setelah permintaan `unveil_secrets`.

### **5. Permintaan `unveil_secrets`:**

* **Kirim Permintaan:**

  * Setelah tanda tangan dikumpulkan dan diverifikasi, permintaan untuk `unveil_secrets` dikirim ke server dengan tanda tangan agregat.
* **Respon Server:**

  * Server merespons dengan error atau tidak memberikan informasi yang diharapkan (seperti yang terlihat pada pesan `Invalid aggregated signature` atau error lainnya).

### **6. Permasalahan yang Terjadi:**

* **Kesalahan pada Verifikasi `sk` dan Pengambilan Data:**

  * Penanganan kesalahan pada verifikasi `sk` buatan server perlu ditingkatkan lebih lanjut.
  * Server tidak selalu mengembalikan `sk` yang valid, atau mungkin ada proteksi yang lebih kuat yang mencegah kebocoran data tersebut.
* **Timeout atau Tidak Ada Respon Setelah Pengiriman `unveil_secrets`:**

  * Ada kalanya server tidak merespon setelah kita mengirimkan permintaan `unveil_secrets`, yang menunjukkan adanya masalah dalam alur komunikasi.

### **Rangkuman Proses:**

* **Keberhasilan:** Kita berhasil membuat robot yang terverifikasi, menggabungkan tanda tangan, dan mendapatkan daftar robot dari server.
* **Kendala:** Beberapa server-made robots tidak mengungkapkan `sk` atau gagal diverifikasi, dan ada kesalahan dalam memproses permintaan setelah pengiriman `unveil_secrets`.
* **Kebutuhan Perbaikan:** Fokus utama adalah memperbaiki cara kita mengekstraksi `sk` dari robot buatan server, menangani verifikasi dengan lebih hati-hati, dan menangani kesalahan atau kesulitan dalam komunikasi server setelah permintaan.

### **Langkah Selanjutnya:**

Untuk lebih meningkatkan kemungkinan mendapatkan `sk` atau flag:

1. **Periksa Lagi Proses Pengambilan `sk`:**

   * Mungkin ada cara lain untuk mendapatkan `sk` (misalnya, jika server mengenkripsi atau mengamankan `sk` menggunakan metode tertentu).
2. **Analisis Lebih Dalam pada Komunikasi Server:**

   * Menganalisis pola komunikasi lebih lanjut, melihat apakah ada cara lain untuk mendapatkan data yang dibutuhkan dari server.
3. **Pertimbangkan Teknik Lain untuk Eksploitasi:**

   * Jika metode eksploitasi saat ini gagal, mungkin ada celah lain (seperti masalah terkait otentikasi atau identifikasi robot).

Dengan terus mencoba pendekatan berbeda, mungkin kita akan menemukan celah yang bisa dimanfaatkan untuk mendapatkan flag.
