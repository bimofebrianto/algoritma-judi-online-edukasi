# 🎲 Algoritma Judi Online (Edukasi)

📌 Repository ini dibuat **untuk edukasi** agar orang tahu bagaimana algoritma judi online bekerja dan kenapa **pemain rata-rata pasti rugi**.  
⚠️ **Bukan untuk membuat sistem judi online!**

---

## ⚠️ PERINGATAN

Repository ini dibuat **hanya untuk tujuan edukasi dan penyadaran**.  

- 🎲 Judi online **dirancang agar pemain selalu kalah**.  
- 💸 Kerugian finansial jangka panjang **tidak bisa dihindari** (Expected Value selalu negatif).  
- 🧠 Risiko kecanduan sangat tinggi, merusak kesehatan mental, pekerjaan, dan hubungan sosial.  
- 👨‍👩‍👧 Banyak keluarga hancur karena judi online.  

🙏 Saya menulis ini **bukan untuk dianggap pahlawan**, tetapi hanya ingin **membantu menyelamatkan orang lain** agar tidak terjerumus ke dalam jebakan judi online.  

---

## 🚫 Saran

- Jangan percaya iklan “menang mudah” atau “cuan instan” dari judi online.  
- Jika ingin mencari penghasilan, pilihlah jalur yang **legal dan sehat** (misalnya investasi emas, saham, reksa dana, atau skill digital).  
- Jika kamu atau orang di sekitarmu sudah kecanduan judi, **cari bantuan**:
  - [WHO: Gambling & Gaming Disorder](https://www.who.int/news-room/fact-sheets/detail/gambling-and-gaming)
  - Konseling lokal / layanan rehabilitasi
  - Dukungan keluarga & teman  

---

## 🔹 Bagaimana Sistem Bekerja

1. **Random Number Generator (RNG)**  
   - Digunakan untuk menghasilkan angka acak.  
   - Pemain percaya hasil acak = adil, tapi sebenarnya selalu ada **house edge**.

2. **House Edge (Keuntungan Rumah)**  
   - Permainan selalu diatur agar keuntungan jangka panjang berpihak ke rumah.  
   - Contoh: peluang menang 49%, kalah 51%, tapi payout dibayar seolah 50:50.  
   - Selisih inilah keuntungan operator.

3. **Expected Value (EV) Negatif**  
   - Rumus:  

     \[
     EV = \sum (p_i \times payout_i) - stake
     \]

   - Jika EV < 0 → pemain selalu rugi rata-rata.

---

## 🔹 Contoh Perhitungan EV

- Peluang menang = 49%  
- Peluang kalah = 51%  
- Payout menang = +1 unit  
- Payout kalah = −1 unit  

\[
EV = (0.49 \times 1) + (0.51 \times -1) = -0.02
\]

👉 Artinya setiap taruhan, pemain rata-rata **kehilangan 2%** dari uang yang dipasang.

---

## 🔹 Simulasi (Folder `simulasi/`)

- `ev.php` → hitung EV sederhana dengan PHP  
- `ev.py` → contoh perhitungan dengan Python  
- `grafik.py` → buat grafik simulasi kerugian jangka panjang  

---

## 🔹 Mengapa Orang Selalu Kalah

- Sekali dua kali bisa menang (karena varians).  
- Tapi makin sering main → hasil semakin mendekati **EV negatif**.  
- **Hukum Bilangan Besar** membuat kerugian pasti muncul.  

---

## 🔹 Tujuan Repo Ini

✅ Memberikan edukasi matematis & teknis.  
✅ Membuka mata bahwa “algoritma adil” bukan berarti bisa menang jangka panjang.  
✅ Mengingatkan: judi online dirancang agar **pemain kalah**.  
✅ Menyebarkan kesadaran agar semakin banyak orang yang **selamat dari jerat judi online**.  

---

## 📖 Sumber Bacaan

- [How Casino Math Works (Wizard of Odds)](https://wizardofodds.com/gambling/house-edge/)  
- [Random Number Generators Explained](https://en.wikipedia.org/wiki/Random_number_generation)  
- [Problem Gambling Help (WHO)](https://www.who.int/news-room/fact-sheets/detail/gambling-and-gaming)  
