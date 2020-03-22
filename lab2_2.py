import random, math
import matplotlib.pyplot as plt
import numpy as np
n = 12 #число гармонік в сигналі
w_gr = 1800 #гранична частота
N = 64 #кількість дискретних відліків

w = w_gr / (n-1)
x = []

def plot(function):
    plt.figure(figsize=(20, 15))
    plt.plot(function)
    plt.grid(True)
    plt.show()

#генерація сигналу
for i in range(n):
    A = random.choice([i for i in range(-10, 10) if i != 0])
    fi = random.randint(-360, 360)
    for t in range(N):
        x_t = A*math.sin((w_gr - i*w)*t+fi)
        x.append(x_t)

# таблиця коефіцієнтів w[p][k] від N/2
w_p_k = np.zeros(shape=(N//2, N//2))
for p in range(N//2):
    for k in range(N//2):
        w_p_k[p][k] = math.cos(4*math.pi/N * p * k) + math.sin(4*math.pi/N * p * k)

# таблиця нових коеф w[p] від N
w_p = np.zeros(N)
for p in range(N):
    w_p[p] = math.cos(2*math.pi/N * p) + math.sin(2*math.pi/N * p)

# непарні
F_odd = np.zeros(N//2)
# парні
F_even = np.zeros(N//2)
# кінцева фнкція
F = np.zeros(N)

# рахуємо окремо для парних і непарних частин функцій
for p in range(N//2):
    for k in range(N//2):
        F_even[p] += x[2*k] * w_p_k[p][k]
        F_odd[p] += x[2*k + 1] * w_p_k[p][k]

for p in range(N):
    if p < (N//2):
        F[p] += F_even[p] + w_p[p] * F_odd[p]
    else:
        F[p] += F_even[p - (N//2)] - w_p[p] * F_odd[p - (N//2)]

plot(F)