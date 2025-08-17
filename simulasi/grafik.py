import random
import matplotlib.pyplot as plt

# Simulasi taruhan dengan EV negatif
prob_win = 0.49
stake = 1
n = 500
saldo = 0
history = []

for i in range(n):
    if random.random() < prob_win:
        saldo += stake
    else:
        saldo -= stake
    history.append(saldo)

plt.plot(history)
plt.title("Simulasi Kerugian Judi Online (EV negatif)")
plt.xlabel("Jumlah Taruhan")
plt.ylabel("Saldo")
plt.show()
