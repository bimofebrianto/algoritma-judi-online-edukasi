# Random Number Generator (RNG)

RNG = algoritma komputer untuk menghasilkan angka acak.  
- Digunakan agar hasil permainan tidak bisa diprediksi pemain.  
- Namun situs tetap menetapkan payout dengan EV negatif.  

Ada konsep *Provably Fair* di beberapa situs:
1. Server membuat "seed" rahasia.
2. Pemain memasukkan "client seed".
3. Kombinasi di-hash → menghasilkan angka acak.
4. Seed server dibuka setelah periode → pemain bisa verifikasi.

⚠️ Meski adil secara teknis, **tetap EV negatif** = pemain tetap kalah rata-rata.
