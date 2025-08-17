# simulasi/ev.py
# ⚠️ Edukasi, bukan untuk praktik judi
# Menghitung Expected Value (EV) sederhana

# Parameter permainan
prob_win = 0.49   # peluang menang
prob_lose = 0.51  # peluang kalah
payout_win = 1    # keuntungan jika menang
payout_lose = -1  # kerugian jika kalah

# Hitung EV
EV = (prob_win * payout_win) + (prob_lose * payout_lose)

print(f"Expected Value per taruhan: {EV:.2f}")
print(f"Artinya: rata-rata rugi {abs(EV*100):.1f}% per taruhan")
